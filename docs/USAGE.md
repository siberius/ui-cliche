# Použití a údržba: ui-cliche v2.0 / Usage and maintenance

Copyright © 2026 Luděk Sušický

## Česky

### Architektura a volba povrchu (Surface Router)

Skill `ui-cliche v2.0` je specializován na krátké funkční texty. Podle typu zpracovávaného obsahu volí jeden ze tří profilů:
1. **`app` (Aplikace a produkty):** Tlačítka, dialogy, chybové hlášky, formuláře, tooltipy a lokalizační soubory (`.json`, `.po`, `.tsx`). Kontroluje dokonavý infinitiv na tlačítkách, činný rod v tooltipech, konzistenci tykání/vykání a pokrytí 6 stavů rozhraní.
2. **`web` (Web a konverzní plochy):** Hero nadpisy, karty vlastností, ceníky, CTA prvky a trust bary. Odstraňuje nepodložené AI superlativy, zákaz anglického Title Case v českých nadpisech a prověřuje pravdivost slibů (*„ihned zdarma“*).
3. **`slides` (Prezentace a decky):** Titulky slidů, odrážkové výčty, callouty a KPI popisky. Vynucuje titulky nesoucí konkrétní zjištění, syntaktickou paralelnost odrážek a jednotnou interpunkci výčtů podle ÚJČ.

> [!WARNING]
> **Omezení záběru (Out-of-Scope):**  
> Dlouhé blogové články, LinkedIn příspěvky, eseje a smlouvy skill **tvrdě odmítá kompletně přepisovat**. V takovém případě nabídne pouze selektivní kontrolu nadpisů a CTA tlačítek.

---

### Spuštění a integrace v agentních nástrojích

#### 1. Instalace přes Skills CLI (skills.sh)
```bash
# Instalace do vybraného agenta (Codex, Claude Code, Cursor atd.)
npx skills add siberius/ui-cliche --full-depth -g -a codex
```

#### 2. Použití v agentních IDE (Codex, Gemini CLI, Cursor, VS Code)
Skill je standardně umístěn v `.agents/skills/ui-cliche/SKILL.md`. Agent načítá manifest automaticky.

#### 3. Použití v Claude Code
Pro Claude Code je připraven nativní symlink `.claude/skills/ui-cliche/SKILL.md`.

#### 4. Webové chaty (Claude Projects, ChatGPT Custom GPT, Gemini Gems)
Pro prostředí bez lokálního souborového systému je připraven optimalizovaný jedno-souborový prompt v [prompts/chat-compact.md](../prompts/chat-compact.md).

---

### Lokální spuštění bezdependenčního linteru

Linter `scripts/ui_lint.py` nevyžaduje žádné balíčky z PyPI (čistý Python 3.9+).

```bash
# Základní spuštění pro aplikaci
python3 scripts/ui_lint.py --surface app src/locales/cs.json

# Spuštění pro webovou stránku s výstupem do formátu JSON
python3 scripts/ui_lint.py --surface web index.html --json

# Spuštění s projektovým slovníkem chráněných termínů
python3 scripts/ui_lint.py --surface app strings.json --keep-terms assets/keep-terms.example.yaml
```

Návratové kódy:
- `0`: Text je čistý (`BEZ ÚPRAV`).
- `1`: Nalezeny tvrdé deterministické blokátory (`hard_lint`).
- `2`: Nalezeni pouze kandidáti k terminologickému posouzení (`soft_candidates`).
- `3`: Chyba vstupu nebo parametrů.

---

### Nastavení chráněných termínů (`keep-terms.yaml`)

Zkopírujte [assets/keep-terms.example.yaml](../assets/keep-terms.example.yaml) do kořene vašeho projektu jako `keep-terms.yaml`. Do souboru můžete přidat:
- **`tone_of_voice.addressing`:** Zvolený tón oslovení (`vykani` nebo `tykani`).
- **`protected_terms`:** Seznam odborných a interních pojmů, na které linter ani model nesmí sahat (např. *prerekvizity*, *robustní šifrování*).
- **`protected_brands`:** Názvy značek a produktů (výjimky z Title Case).

---

## English

### Architecture and Surface Routing

`ui-cliche v2.0` is engineered specifically for functional microcopy:
- **`app`:** UI buttons (perfective infinitives), tooltips (active voice), 6 interface states, addressing consistency (tykání/vykání), and i18n placeholders.
- **`web`:** Hero headlines (no Title Case in Czech), feature cards, proof-backed value propositions, CTA commitment verification.
- **`slides`:** Finding-driven slide titles, syntactically parallel bullet points, ÚJČ AV ČR / ČSN 01 6910 bullet punctuation profiles.

Long prose, blog posts, essays, and legal documents are **strictly rejected from full rewrites**.
