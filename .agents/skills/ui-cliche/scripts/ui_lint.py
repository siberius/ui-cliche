#!/usr/bin/env python3
"""
ui_lint.py - Deterministický linter českých mikrotextů v UI, na webu a slidech.

Autor: Luděk Sušický (MIT License)
Metodická inspirace:
  - Architektura bezdependenčního deterministického linteru a párového testování
    po vzoru projektu kalky (Zdeněk Dvořák, MIT).
  - Princip oddělení tvrdých vad od nezávazných kandidátů k posouzení
    po vzoru projektu Korektor (David Fogl / Continero).
Implementace parseru, maskování i18n proměnných, profilů výčtů ÚJČ a pravidel pro rozhraní:
  Původní autorský kód pro projekt ui-cliche v2.0.

Standard: Python 3.9+ bez externích závislostí.
Vrací:
  0 - Čistý text (žádné vady ani podezřelí kandidáti -> verdikt BEZ ÚPRAV)
  1 - Nalezeny tvrdé deterministické blokátory (hard_lint)
  2 - Nalezeni pouze měkcí kandidáti k posouzení (soft_candidates)
  3 - Chyba vstupu nebo parametrů
"""

import argparse
import json
import os
import re
import sys
from typing import Any, Dict, List, Optional, Set, Tuple

# Regulární výrazy pro maskování proměnných a značek
RE_ICU_PLACEHOLDER = re.compile(r"\{[^{}]*\}")
RE_DOUBLE_CURLY = re.compile(r"\{\{[^{}]*\}\}")
RE_PRINTF = re.compile(r"%(?:\([a-zA-Z0-9_]+\))?[0-9]*\.?[0-9]*[sfdxX]")
RE_HTML_TAG = re.compile(r"<[^>]+>")

# Pravidla pro tvrdé deterministické vady (hard_lint)
RE_EM_DASH = re.compile(r"—")
RE_AI_FILLER = re.compile(
    r"\b(v dnešní uspěchané době|pojďme se ponořit|v tomto článku se podíváme|"
    r"je důležité si uvědomit|v dnešním digitálním světě|v dynamickém světě)\b",
    re.IGNORECASE,
)
RE_TRAILING_BUTTON_PERIOD = re.compile(r"^([\w\s\-\–]{1,35})\.$", re.UNICODE)
RE_TITLE_CASE = re.compile(
    r"\b([A-ZÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ][a-záčďéěíňóřšťúůýž]+)\s+([A-ZÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ][a-záčďéěíňóřšťúůýž]+(?:\s+[A-ZÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ][a-záčďéěíňóřšťúůýž]+)*)\b"
)

# Pravidla pro měkké kandidáty k posouzení (soft_candidate)
SOFT_PATTERNS = [
    ("prerekvizit", "prerekvizit", "domain_bound", "V univerzitním IS zachovat. V SaaS/webu nahradit: 'co potřebujete předem', 'nutné podmínky'."),
    ("hygienický standard", r"hygienick[ýééhoémmu]*\s+standard", "shifted_calque", "Ve zdravotnictví zachovat. V HR teorii 'hygienické faktory'. Na webu/SaaS 'samozřejmý základ', 'nezbytné minimum'."),
    ("mrtvé adresy", r"mrtv[éých]*\s+(?:adres|odkaz)", "unsettled_calque", "Vždy nahradit zavedeným českým pojmem: 'neexistující stránky (chyba 404)', 'nefunkční odkazy'."),
    ("robustní", r"\brobustn[ííhoémuých]*\b", "buzzword_or_domain", "Posoudit: stojí u pojmu konkrétní důkaz (např. robustní šifrování AES-256), nebo jde o prázdné AI adjektivum?"),
    ("komplexní", r"\bkomplexn[ííhoémuých]*\b", "buzzword_or_domain", "Posoudit: jde o přesný odborný pojem (komplexní vyšetření), nebo vágní vatu?"),
    ("klíčový", r"\bklíčov[ýééhoémuých]*\b", "buzzword_or_domain", "Posoudit: technická 'klíčová metrika' vs. prázdné zdůraznění."),
    ("řešení", r"\břešení\b", "buzzword_or_domain", "Posoudit: konkrétní technické řešení vs. generický marketingový balast."),
    ("upsík", r"\bupsík\b|\boups\b", "inappropriate_humor", "Zákaz necitlivého humoru v chybových a platebních stavech."),
    ("klikněte zde", r"\bklikn[ěu]te\s+zde\b|\bzde\b", "bad_link_text", "Odkazy musí pojmenovávat cíl, nikoli mechanickou akci."),
    ("zjistit více", r"^(?:zjistit\s+více|více)$", "bad_link_text", "Nahradit popisem cílové stránky."),
    ("ihned / zdarma", r"\b(ihned|zdarma|bez registrace)\b", "commitment_guard", "Ověřit pravdivost závazku: je služba skutečně ihned / zdarma bez skrytých podmínek?"),
]

# Známá česká vlastní jména pro výjimky z Title Case
WHITELIST_PROPER_NOUNS = {
    "Česká republika", "Evropská unie", "Karlova univerzita", "Google Cloud",
    "OpenAI", "Microsoft", "Claude", "Gemini", "Apple", "Linux", "Windows",
}


class TextMasker:
    """Maskuje dynamické zástupné symboly, i18n proměnné a HTML tagy."""

    def __init__(self):
        self.placeholders: List[str] = []

    def mask(self, text: str) -> str:
        self.placeholders.clear()

        def repl(match):
            token = f"__PH_{len(self.placeholders)}__"
            self.placeholders.append(match.group(0))
            return token

        # Maskování složených ICU závorek {{user}} a {count}
        res = RE_DOUBLE_CURLY.sub(repl, text)
        res = RE_ICU_PLACEHOLDER.sub(repl, res)
        res = RE_PRINTF.sub(repl, res)
        res = RE_HTML_TAG.sub(repl, res)
        return res

    def unmask(self, text: str) -> str:
        res = text
        for idx, orig in enumerate(self.placeholders):
            res = res.replace(f"__PH_{idx}__", orig)
        return res


def load_keep_terms(path: Optional[str]) -> Set[str]:
    """Načte seznam chráněných termínů ze souboru YAML nebo JSON."""
    if not path or not os.path.exists(path):
        return set()
    terms: Set[str] = set()
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        # Zkusíme JSON
        try:
            data = json.loads(content)
            if isinstance(data, list):
                terms.update(str(x).lower().strip() for x in data)
            elif isinstance(data, dict):
                for k, v in data.items():
                    if isinstance(v, list):
                        terms.update(str(x).lower().strip() for x in v)
                    elif isinstance(v, str):
                        terms.add(v.lower().strip())
        except Exception:
            # Jednoduchý YAML fallback (řádky s - nebo klíče)
            for raw_line in content.splitlines():
                line = raw_line.strip()
                if "#" in line:
                    line = line.split("#", 1)[0].strip()
                if not line:
                    continue
                if line.startswith("- "):
                    val = line[2:].strip().strip("\"'").lower()
                    if val:
                        terms.add(val)
                elif ":" in line and not line.startswith("#"):
                    parts = line.split(":", 1)
                    val = parts[1].strip().strip("\"'").lower()
                    if val:
                        terms.add(val)
    except Exception as e:
        sys.stderr.write(f"Varování: nelze načíst keep-terms z {path}: {e}\n")
    return terms


def extract_strings_from_json(obj: Any, path: str = "") -> List[Tuple[str, str, int]]:
    """Rekurzivně vyextrahuje textové řetězce z i18n JSON struktury."""
    results = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            subpath = f"{path}.{k}" if path else k
            results.extend(extract_strings_from_json(v, subpath))
    elif isinstance(obj, list):
        for idx, item in enumerate(obj):
            subpath = f"{path}[{idx}]"
            results.extend(extract_strings_from_json(item, subpath))
    elif isinstance(obj, str):
        results.append((path, obj, 1))
    return results


def check_list_punctuation(lines: List[str]) -> List[Dict[str, Any]]:
    """Kontrola jednotnosti interpunkce odrážkových seznamů (Profily A–D dle ÚJČ)."""
    findings = []
    current_block: List[Tuple[int, str]] = []

    def flush_block(block: List[Tuple[int, str]]):
        if len(block) < 2:
            return
        has_period = 0
        has_comma_semicolon = 0
        has_none = 0
        for line_no, text in block:
            cleaned = text.strip()
            if cleaned.endswith(".") or cleaned.endswith("!") or cleaned.endswith("?"):
                has_period += 1
            elif cleaned.endswith(",") or cleaned.endswith(";"):
                has_comma_semicolon += 1
            else:
                has_none += 1

        total_items = len(block)
        last_item_text = block[-1][1].strip()

        # 1. Platný Profil A: vše bez interpunkce
        if has_none == total_items:
            return

        # 2. Platný Profil C: vše samostatné věty s tečkou (nebo ? / !)
        if has_period == total_items:
            return

        # 3. Platný Profil B: položky 1..(N-1) mají čárku/středník a pouze poslední má tečku
        if (
            has_comma_semicolon == total_items - 1
            and (last_item_text.endswith(".") or last_item_text.endswith("!") or last_item_text.endswith("?"))
            and has_none == 0
        ):
            return

        # Jinak jde o nekonzistentní smíšený výčet (Profil D / porušení ÚJČ)
        findings.append({
            "rule_id": "LIST_MIXED_PUNCTUATION",
            "line": block[0][0],
            "found": f"Smíšený výčet: {has_period} s tečkou, {has_comma_semicolon} s čárkou/středníkem, {has_none} bez interpunkce",
            "expected": "Jednotný profil dle ÚJČ/ČSN 01 6910: buď Profil A (vše bez tečky), Profil B (čárky + závěrečná tečka), nebo Profil C (vše plné věty s tečkou).",
            "message": "Nekonzistentní interpunkce položek seznamu v rámci jednoho výčtu.",
        })

    for line_idx, raw_line in enumerate(lines, start=1):
        stripped = raw_line.strip()
        if re.match(r"^[-*•]\s+", stripped) or re.match(r"^\d+\.\s+", stripped):
            content = re.sub(r"^[-*•]\s+|\d+\.\s+", "", stripped)
            current_block.append((line_idx, content))
        else:
            if current_block:
                flush_block(current_block)
                current_block = []
    if current_block:
        flush_block(current_block)

    return findings


def lint_content(
    content: str,
    surface: str,
    keep_terms: Set[str],
    is_json_file: bool = False,
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], int]:
    """Hlavní analytická funkce provádějící deterministickou kontrolu."""
    hard_lint: List[Dict[str, Any]] = []
    soft_candidates: List[Dict[str, Any]] = []
    masker = TextMasker()

    items_to_check: List[Tuple[int, str, str]] = []  # (line_num, text, context_label)

    if is_json_file:
        try:
            data = json.loads(content)
            extracted = extract_strings_from_json(data)
            for path_key, val_str, _ in extracted:
                items_to_check.append((1, val_str, path_key))
        except Exception as e:
            raise ValueError(f"Chyba při parsování JSON: {e}")
    else:
        raw_lines = content.splitlines()
        # Kontrola seznamů na úrovni celého souboru
        list_findings = check_list_punctuation(raw_lines)
        hard_lint.extend(list_findings)

        for idx, line in enumerate(raw_lines, start=1):
            items_to_check.append((idx, line, f"řádek {idx}"))

    total_tokens = 0

    for line_no, raw_text, ctx_label in items_to_check:
        masked = masker.mask(raw_text)
        words = masked.split()
        total_tokens += len(words)

        # 1. HARD LINT: Dlouhá pomlčka (—)
        if RE_EM_DASH.search(masked):
            hard_lint.append({
                "rule_id": "TYPO_EM_DASH",
                "line": line_no,
                "context": ctx_label,
                "found": "—",
                "expected": "–",
                "message": "Nalezena dlouhá pomlčka (—). V české typografii používejte krátkou pomlčku (–) s mezerami.",
            })

        # 2. HARD LINT: AI filler / odkašlávací fráze
        m_filler = RE_AI_FILLER.search(masked)
        if m_filler:
            hard_lint.append({
                "rule_id": "AI_FILLER_INTRO",
                "line": line_no,
                "context": ctx_label,
                "found": m_filler.group(0),
                "expected": "Přejít přímo k věci / smazat úvodní vatu.",
                "message": f"Nalezena generická strojová výplň: '{m_filler.group(0)}'.",
            })

        # 3. HARD LINT: Tečka za krátkým tlačítkem / samostatným popiskem
        # Uplatňuje se v režimu app nebo u krátkých izolovaných řetězců
        cleaned_text = masked.strip()
        if (surface == "app" or is_json_file) and len(words) <= 4:
            m_btn = RE_TRAILING_BUTTON_PERIOD.match(cleaned_text)
            if m_btn:
                base_txt = m_btn.group(1).strip()
                # Výjimka pro výpustky (tři tečky / trojtečka)
                if not base_txt.endswith("…") and not base_txt.endswith(".."):
                    hard_lint.append({
                        "rule_id": "UI_BUTTON_PERIOD",
                        "line": line_no,
                        "context": ctx_label,
                        "found": cleaned_text,
                        "expected": base_txt,
                        "message": "Samostatné tlačítko nebo popisek nesmí končit tečkou.",
                    })

        # 4. HARD LINT: Anglický Title Case v českých nadpisech
        # Pokud má text 2 až 8 slov a obsahuje více po sobě jdoucích velkých písmen
        if len(words) >= 2 and len(words) <= 10:
            tc_match = RE_TITLE_CASE.search(cleaned_text)
            if tc_match:
                full_tc = tc_match.group(0)
                # Ověříme, zda nejde o schválené vlastní jméno z whitelistu
                if full_tc not in WHITELIST_PROPER_NOUNS:
                    # Pokud druhé a další slovo nejsou běžné zkratky
                    second_words = full_tc.split()[1:]
                    if any(w.islower() is False and len(w) > 2 for w in second_words):
                        hard_lint.append({
                            "rule_id": "TYPO_TITLE_CASE",
                            "line": line_no,
                            "context": ctx_label,
                            "found": full_tc,
                            "expected": full_tc.capitalize(),
                            "message": f"Zjištěna anglická velkopísmenná kapitalizace (Title Case): '{full_tc}'. V češtině začíná velkým písmenem pouze první slovo.",
                        })

        # 5. SOFT CANDIDATES: Prověření podezřelých termínů
        text_lower = cleaned_text.lower()
        for term_label, pattern_str, cat, guidance in SOFT_PATTERNS:
            # Kontrola whitelistu chráněných termínů
            if term_label.lower() in keep_terms or any(kt in text_lower for kt in keep_terms):
                continue

            matches = list(re.finditer(pattern_str, text_lower, re.IGNORECASE))
            for match in matches:
                found_word = match.group(0)
                if found_word in keep_terms:
                    continue
                soft_candidates.append({
                    "rule_id": "TERM_TRIAGE_CANDIDATE",
                    "term": found_word,
                    "category": cat,
                    "line": line_no,
                    "context": ctx_label,
                    "snippet": cleaned_text[:120],
                    "guidance": guidance,
                })

    return hard_lint, soft_candidates, total_tokens


def main():
    parser = argparse.ArgumentParser(description="Deterministický linter českých mikrotextů.")
    parser.add_argument("input_path", help="Cesta k souboru (nebo '-' pro standardní vstup)")
    parser.add_argument("--surface", choices=["app", "web", "slides"], default="app", help="Typ povrchu")
    parser.add_argument("--keep-terms", help="Cesta k souboru chráněných termínů (keep-terms.yaml/json)")
    parser.add_argument("--json", action="store_true", help="Výstup ve formátu JSON")

    args = parser.parse_args()

    content = ""
    is_json_file = False

    if args.input_path == "-":
        content = sys.stdin.read()
    else:
        if not os.path.exists(args.input_path):
            sys.stderr.write(f"Chyba: Soubor {args.input_path} neexistuje.\n")
            sys.exit(3)
        if args.input_path.endswith(".json"):
            is_json_file = True
        try:
            with open(args.input_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            sys.stderr.write(f"Chyba při čtení souboru: {e}\n")
            sys.exit(3)

    keep_terms = load_keep_terms(args.keep_terms)

    try:
        hard_lint, soft_candidates, total_tokens = lint_content(
            content=content,
            surface=args.surface,
            keep_terms=keep_terms,
            is_json_file=is_json_file,
        )
    except Exception as e:
        sys.stderr.write(f"Chyba analýzy: {e}\n")
        sys.exit(3)

    if args.json:
        result = {
            "surface": args.surface,
            "stats": {
                "tokens_analyzed": total_tokens,
                "hard_count": len(hard_lint),
                "soft_count": len(soft_candidates),
            },
            "hard_lint": hard_lint,
            "soft_candidates": soft_candidates,
        }
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"=== Výsledky linteru ui-cliche v2.0 (povrch: {args.surface}) ===")
        print(f"Analyzováno tokenů: {total_tokens}")
        print()
        if hard_lint:
            print(f"❌ BLOKÁTORY (Hard Lint) - {len(hard_lint)} nálezů:")
            for h in hard_lint:
                print(f"  • [{h['rule_id']}] {h.get('context', '')}: {h['message']}")
                print(f"    Nalezeno: '{h.get('found', '')}' -> Očekáváno: '{h.get('expected', '')}'")
            print()
        else:
            print("✅ Žádné tvrdé deterministické blokátory nebyly nalezeny.")
            print()

        if soft_candidates:
            print(f"⚠️ K POSOUZENÍ (Soft Candidates pro LLM) - {len(soft_candidates)} kandidátů:")
            for s in soft_candidates:
                print(f"  • Výraz: '{s['term']}' ({s['category']}) na {s.get('context', '')}")
                print(f"    Vodítko: {s['guidance']}")
                print(f"    Úryvek: \"{s['snippet']}\"")
            print()
        else:
            print("ℹ️ Žádní kandidáti k terminologickému posouzení.")

        if not hard_lint and not soft_candidates:
            print("🟢 VÝSLEDEK: BEZ ÚPRAV (text splňuje všechna pravidla)")

    if hard_lint:
        sys.exit(1)
    elif soft_candidates:
        sys.exit(2)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
