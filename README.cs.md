# UI Klišé v2.0: Nativní český editor mikrotextů a slidů
*(Czech Surface-Aware Microcopy & Slide Editing for AI Agents)*

[Česky](README.cs.md) · [English](README.md)  
[![Skills.sh](https://img.shields.io/badge/skills.sh-Install-blue)](https://skills.sh/siberius/ui-cliche)
[![Agent Skills AAIF](https://img.shields.io/badge/Agent%20Skills-AAIF%20Standard-success)](https://agentskills.io)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> 📖 **Článek a kontext na Vibemaker:** [Texty rozhraní bez AI klišé](https://vibemaker.cz/clanek/psani-bez-ai-otisku/)

`ui-cliche v2.0` je specializovaný agentní skill a hybridní linter pro **nativní češtinu v aplikacích, na webu a v prezentacích**. Oproti univerzálním promptům odpojuje posuzování od anglických šablon a zaměřuje se čistě na specifické vady funkčních textů: gramatiku českých tlačítek a tooltipů, pravdivost závazků v CTA prvcích, jednotnost interpunkce výčtů podle ÚJČ AV ČR a ČSN 01 6910, třístupňovou triáž pseudoodborných kalků a bezpečnou ochranu i18n proměnných.

Splňuje otevřený standard **Agent Skills (AAIF)** a nativně funguje v nástrojích **Claude Code, OpenAI Codex, Gemini CLI, Cursor i VS Code**.

---

## Výsledky evaluačního benchmarku (v2.0)

Měření na zlaté sadě 15 behaviorálních scénářů a 24 testech spuštění (`evals/benchmark.json`):

| Metrika a testovací koš | Výchozí stav (v1.x) | ui-cliche v2.0 | Cílový požadavek | Stav |
|---|---|---|---|---|
| **Záchyt vad a AI klišé (Koš A – Recall)** | ~70 % | **100,0 %** | $\ge 90\,\%$ | ✅ Splněno |
| **Plané nálezy na lidském textu (Koš B – FPR)** | 25–35 % *(přepisoval platné termíny)* | **0,0 %** | $< 5\,\%$ | ✅ Špičkový výsledek |
| **Ochrana i18n ICU a HTML syntaxe (Koš C)** | Křehká (riziko překladu proměnných) | **100,0 %** | $100\,\%$ | ✅ Bezpečná |
| **Přesnost spuštění (Trigger Evals)** | Neověřeno | **100,0 %** *(24/24 dotazů)* | $\ge 90\,\%$ | ✅ Ostré hranice |
| **Průměrná latence linteru** | — | **~50 ms** *(Python 3.9+)* | $< 200\text{ ms}$ | ✅ Bleskový běh |

---

## Co skill řeší a co striktně odmítá

| Povrch (Surface) | V záběru (In-Scope) | Co skill kontroluje |
|---|---|---|
| **Aplikace (App UI)** | Tlačítka, formuláře, nápovědy, tooltipy, prázdné stavy, chybové hlášky, i18n (`.json`, `.po`, `.tsx`). | Dokonavý infinitiv (*Uložit*), činný rod v tooltipech, jednotné oslovení (tykání/vykání), pokrytí 6 stavů rozhraní, zákaz humoru typu *„Upsík“* u plateb. |
| **Web a konverze (Web)** | Hero nadpisy, karty funkcí, ceníky, CTA prvky, trust bary, FAQ. | Odstranění nepodložených superlativů, zákaz anglického *Title Case*, ověření pravdivosti slibů (*ihned*, *zdarma*). |
| **Prezentace (Slides)** | Titulky slidů, odrážkové výčty, callout boxy, KPI popisky. | Titulky nesoucí věcné zjištění, syntaktická paralelnost odrážek, jednotná interpunkce výčtů dle ÚJČ. |
| **MIMO ZÁBĚR (Out-of-Scope)** | **Blogové články, LinkedIn příspěvky, eseje, smlouvy, e-maily nad 300 slov.** | **Tvrdé odmítnutí plného přepisu.** Upozorní na specializaci na mikrotexty a nabídne pouze selektivní kontrolu nadpisů a tlačítek. |

---

## 6 klíčových architektonických inovací

1. **Dvoustupňový hybridní model (Linter + Adjudikátor):** Bezdependenční Python skript (`scripts/ui_lint.py`) odhalí mechanické vady (`hard_lint`) a vytipuje podezřelé kandidáty (`soft_candidate`). LLM v roli adjudikátora posuzuje kontext a doménu. Je-li text čistý, vrací verdikt `BEZ ÚPRAV`.
2. **Třístupňová terminologická triáž:**
   - *Doménově vázané termíny:* Např. *prerekvizity* v univerzitním IS zůstávají zachovány; v běžném SaaS se nahrazují za *co potřebujete předem*.
   - *Posunuté kalky:* Např. *hygienický standard* v medicíně zůstává; na produktovém webu se mění na *samozřejmý základ*.
   - *Neusazené kalky:* Např. *mrtvé adresy* se vždy nahrazují za *nefunkční odkazy (chyba 404)*.
   - *Absolutní zákaz neologismů:* Pokud není znám český ekvivalent, rozloží se na konkrétní sloveso a předmět.
3. **Čtyři interpunkční profily výčtů dle ÚJČ AV ČR a ČSN 01 6910:**
   - *Profil A (heslovitý):* Bez dvojtečky, velká písmena, **žádná tečka ani čárka** na konci (výchozí pro UI).
   - *Profil B (syntakticky navázaný):* Dvojtečka, malá písmena, čárky/středníky, tečka pouze na konci.
   - *Profil C (větný):* Celé věty, velká písmena, tečky za každým bodem.
   - *Profil D (normalizace smíšených výčtů):* Návrh sjednocení struktury.
4. **Audit pravdivosti UX závazků (*Commitment Guard*):** Zákaz nepodložených tvrzení typu *„ihned zdarma“*, pokud následuje zadání platební karty. Vkládání štítku `[ověřit obchodní podmínku]`.
5. **Projektový whitelist (`keep-terms.yaml`):** Možnost definovat chráněné výrazy týmu, na které linter ani model nesmí sáhnout.
6. **Progresivní odkrývání (Token Economy):** Načítání pouze aktivního povrchu (`surface-app.md`, `surface-web.md`, `surface-slides.md`) šetří kontextové okno modelu.

---

## Instalace a rychlé spuštění

### 1. Instalace přes Skills CLI (skills.sh)
```bash
# Instalace do libovolného agenta (např. codex, claude-code, gemini-cli)
npx skills add siberius/ui-cliche --full-depth -g -a codex
```

### 2. Standardní agentní cesty (AAIF / Claude Code / Cursor)
- **Codex, Gemini CLI, Cursor, VS Code:** Skill je umístěn v `.agents/skills/ui-cliche/SKILL.md`.
- **Claude Code:** Využívá připravený symlink `.claude/skills/ui-cliche/SKILL.md`.

### 3. Spuštění lokálního linteru v terminálu
```bash
# Kontrola UI souboru aplikace
python3 scripts/ui_lint.py --surface app cesty/k/souboru.json

# Kontrola webové stránky s výstupem do JSONu
python3 scripts/ui_lint.py --surface web index.html --json

# Kontrola s vlastním whitelistovým slovníkem
python3 scripts/ui_lint.py --surface app src/locales/cs.json --keep-terms keep-terms.yaml
```

---

## Struktura repozitáře

```
ui-cliche/
├── .agents/skills/ui-cliche/
│   └── SKILL.md                          # Řídicí manifest (<250 řádků)
├── references/
│   ├── surface-app.md                    # Pravidla pro UI aplikace a 6 stavů
│   ├── surface-web.md                    # Pravidla pro konverzní weby a CTA
│   ├── surface-slides.md                 # Pravidla pro titulky a odrážky slidů
│   ├── cs-lexicon-triage.md              # 3stupňová triáž kalků a falešných přátel
│   └── cs-typography-lists.md            # Profily výčtů A–D ÚJČ / ČSN 01 6910
├── scripts/
│   ├── ui_lint.py                        # Bezdependenční Python 3.9+ linter
│   └── run_evals.py                      # Spouštěč evalů a benchmarku
├── assets/
│   └── keep-terms.example.yaml           # Šablona chráněných doménových pojmů
├── evals/
│   ├── trigger_evals.json                # 24 testů spuštění (in-scope / out-of-scope)
│   ├── evals.json                        # 15 zlatých behaviorálních scénářů
│   ├── benchmark.json                    # Výsledky benchmarku a naměřené metriky
│   └── corpus/                           # Testovací soubory pro Koš A, B i C
├── tests/
│   └── test_ui_lint.py                   # 19 jednotkových testů s protipříklady
└── prompts/
    └── chat-compact.md                   # Kompaktní verze pro Claude Projects / Custom GPT
```

---

### Autor

**Luděk Sušický** — biolog, středoškolský a vysokoškolský učitel informatických předmětů

- E-mail: [ludek.susicky@gmail.com](mailto:ludek.susicky@gmail.com)
- X: [@ludeksusicky](https://x.com/ludeksusicky)
- LinkedIn: [Luděk Sušický](https://www.linkedin.com/in/ludek-susicky/)
- GitHub: [@siberius](https://github.com/siberius) — další vzdělávací projekty a otevřené aplikace

---

## Licence

MIT License · Copyright © 2026 Luděk Sušický. Viz [LICENSE](LICENSE).
