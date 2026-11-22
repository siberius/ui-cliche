---
name: ui-cliche
description: >-
  Audituje a upravuje krátké české texty v uživatelských rozhraních aplikací
  (tlačítka, formuláře, chybové hlášky, i18n), na webových stránkách (hero,
  karty, CTA, ceníky) a v prezentacích (titulky a odrážky slidů). Odstraňuje
  AI klišé, anglické kalky, pseudoodborné termíny a nekonzistentní českou
  interpunkci výčtů podle ÚJČ/ČSN 01 6910 při zachování platné odborné
  terminologie. Použít při revizi UI mikrotextů, webových sekcí a slidů.
  NEPOUŽÍVAT pro dlouhé články, blogy, LinkedIn posty ani právní dokumenty.
license: MIT
compatibility: Python 3.9+ (volitelný pro scripts/ui_lint.py); funguje i čistě instrukčně.
metadata:
  version: "2.0.0"
  language: "cs"
---

# Český editor mikrotextů pro aplikace, weby a prezentace

## Tvrdá omezení (nepřekročitelné hranice)
- **NIKDY** nepřepisuj dlouhé články, e-maily nad 300 slov ani příspěvky na sociální sítě. Pokud uživatel vloží dlouhý text, upozorni na vymezení skillu a nabídni pouze kontrolu nadpisů, odrážkových výčtů a CTA.
- **NIKDY** nemaž ani nenahrazuj termíny uvedené v `keep-terms.yaml` nebo doložitelně zavedené v doméně uživatele (např. *prerekvizita* v univerzitním IS, *hygienický faktor* v HR teorii, *robustní šifrování* v bezpečnostním popisu).
- **VŽDY** upřednostni verdikt `BEZ ÚPRAV`, pokud je původní lidský text srozumitelný, věcně přesný a typograficky jednotný. Nevymýšlej úpravy jen proto, abys vykázal aktivitu.
- **NIKDY** neměň fakta, čísla, právní závazky ani i18n proměnné (`{count}`, `{{user}}`, `%s`, HTML tagy). Chybějící důkaz označ `[ověřit obchodní podmínku]` nebo `[doplnit: …]`.
- **NIKDY** nevytvářej nové české neologismy ani pseudoodborné složeniny. Při náhradě pseudotermínu použij zavedený český výraz nebo prostý popis (činné sloveso + předmět).
- **NIKDY** svévolně nerozsekávej souvislé věty do odrážek, pokud to přímo nevyžaduje struktura komponenty.

## Pracovní postup (4 kroky)
1. **Urči povrch (`app` / `web` / `slides`)** a načti POUZE odpovídající soubor z `references/surface-*.md` a společný `references/cs-typography-lists.md`.
2. **Spusť deterministický předfiltr** (je-li dostupný shell):
   ```bash
   python3 scripts/ui_lint.py --surface <app|web|slides> --json <soubor>
   ```
   Získej výstup `hard_lint` (blokátory) a `soft_candidates` (kandidáti k adjudikaci).
3. **Proveď kontextovou adjudikaci** podle `references/cs-lexicon-triage.md`:
   - Prověř každý `soft_candidate` proti doméně a okolnímu důkazu. Je-li výraz v doméně platný a podložený, zamítni nález a zařaď jej do sekce **Zachováno (ověřeno)**.
   - Zkontroluj jednotnost interpunkce výčtů (Profily A–D).
   - V režimu `app` ověř konzistenci oslovení (tykání vs. vykání) a pokrytí 6 stavů rozhraní.
4. **Vypiš tříúrovňový diff** (Blokátory / K posouzení / Zachováno) s důvodem a návrhem. Teprve po schválení uživatelem (nebo při explicitním přepínači `--apply`) generuj finální přepis.

## Šablona výstupu

Pokud je text v pořádku a nevykazuje žádné vady:
```markdown
### Výsledek auditu
🟢 **BEZ ÚPRAV**: Text je věcně přesný, terminologicky platný a typograficky jednotný.
```

Pokud byly nalezeny vady či podněty k úpravě:
```markdown
### Výsledek auditu: ui-cliche v2.0 (povrch: <app | web | slides>)

#### 1. Blokátory (jednoznačné chyby k opravě)
- **[Kategorie / Pravidlo]** `Původní text` -> `Návrh opravy`  
  *Důvod:* Vysvětlení vady (např. dlouhá pomlčka, tečka za tlačítkem, anglický Title Case, klamavý závazek).

#### 2. K posouzení (potenciální klišé a pseudotermíny)
- **[Výraz]** `Původní text` -> `Doporučená alternativa`  
  *Kontext a důvod:* Proč výraz působí nepřirozeně a jakou funkci má alternativa.

#### 3. Zachováno (ověřená doménová terminologie)
- **[Termín]** Ponecháno v původní podobě (např. *prerekvizity*, *robustní šifrování*).  
  *Důvod:* Termín je v dané oborové doméně platný a přesný.
```
