# Výsledky benchmarku a evaluační metodika: ui-cliche v2.0

Copyright © 2026 Luděk Sušický

Tento dokument detailně popisuje čtyřvrstvou evaluační architekturu, testovací metodiku a reprodukovatelné výsledky benchmarku pro skill `ui-cliche v2.0`.

---

## 1. Architektura evaluačního rámce

Přestavba na verzi 2.0 staví na metodice **Evals First** a propojuje:
1. Metodiku Anthropic *skill-creator* pro behaviorální scénáře.
2. Deterministické testování s povinnými protipříklady po vzoru projektu *kalky* (Zdeněk Dvořák).
3. Striktní testování na negativním korpusu autentických lidských textů (Koš B) pro eliminaci planých poplachů.

```
                  ┌────────────────────────────────────────┐
                  │ 1. Testy aktivace (trigger_evals.json) │
                  │  24 reálných dotazů (12 v / 12 mimo)   │
                  └──────────────────┬─────────────────────┘
                                     │
                                     ▼
                  ┌────────────────────────────────────────┐
                  │ 2. Unit testy linteru (test_ui_lint.py)│
                  │  19 testů: pozitivní vzor + protipříklad│
                  └──────────────────┬─────────────────────┘
                                     │
                                     ▼
                  ┌────────────────────────────────────────┐
                  │ 3. Zlatý korpus (evals.json + corpus/) │
                  │   15 scénářů ve 3 koších (A, B, C)     │
                  └──────────────────┬─────────────────────┘
                                     │
                                     ▼
                  ┌────────────────────────────────────────┐
                  │ 4. Automatický vyhodnocovač & report   │
                  │  scripts/run_evals.py -> benchmark.json│
                  └────────────────────────────────────────┘
```

---

## 2. Souhrnné výsledky benchmarku

Výsledky běhu evaluační sady (`scripts/run_evals.py` generující `evals/benchmark.json`):

| Metrika a testovací koš | Cíl | Naměřeno (v2.0) | Stav |
|---|---|---|---|
| **Záchyt vad a AI klišé (Koš A – Recall)** | $\ge 90\,\%$ | **100,0 %** *(6/6 scénářů)* | ✅ Splněno |
| **Plané nálezy na lidském textu (Koš B – FPR)** | $< 5\,\%$ | **0,0 %** *(0/5 falešných blokátorů)* | ✅ Špičková specificita |
| **Ochrana i18n ICU a HTML syntaxe (Koš C)** | $100\,\%$ | **100,0 %** *(4/4 scénářů)* | ✅ Beze změny syntaxe |
| **Přesnost aktivace (Trigger Evals)** | $\ge 90\,\%$ | **100,0 %** *(24/24 dotazů)* | ✅ Ostrá hranice záběru |
| **Průměrná latence linteru** | $< 200\text{ ms}$ | **~40–50 ms** *(Python 3.9+)* | ✅ Bleskový běh |

---

## 3. Detailní rozpad scénářů ve zlatém korpusu

### Koš A: Pozitivní testy (Záchyt vad a AI klišé)
Cílem je ověřit 100% záchyt typografických vad, marketingového slopu, nepatřičného humoru a pseudotermínů:

| ID scénáře | Testovací soubor | Typ povrchu | Klíčové ověření | Výsledek |
|---|---|---|---|---|
| `pos_01_saas_landing` | `messy_saas_landing.html` | `web` | Záchyt Title Case v nadpisu, odhalení superlativů bez důkazu, záchyt generického klišé odkašlání. | ✅ PASS |
| `pos_02_modal_imperative` | `messy_modal_imperative.json` | `app` | Záchyt koncových teček za tlačítky, rozkazovacího způsobu tlačítek a nevhodného humoru *„Upsík“*. | ✅ PASS |
| `pos_03_slides_bullets` | `messy_slides_bullets.md` | `slides` | Záchyt nekonzistentní interpunkce odrážek, triáž nepatřičných *prerekvizit* v prodeji a kalku *mrtvé adresy*. | ✅ PASS |
| `pos_04_bad_link_texts` | `messy_links.json` | `app` | Odhalení nicneříkajících textů odkazů (*„Více“*, *„Klikněte zde“*). | ✅ PASS |
| `pos_05_unverified_cta` | `messy_cta_commitments.json` | `web` | Odhalení nepodloženého závazku *„ihned zdarma“* se zástupnou značkou `[ověřit obchodní podmínku]`. | ✅ PASS |
| `pos_06_em_dashes` | `messy_typography_dashes.md` | `app` | 100% záchyt dlouhých pomlček (`—`) a návrh náhrady za českou krátkou pomlčku (`–`). | ✅ PASS |

### Koš B: Negativní testy (Čisté lidské texty – True Negative)
Cílem je prokázat, že skill **neprovádí neoprávněné kosmetické přepisy** na přirozených a správných lidských textech (FPR = 0,0 %):

| ID scénáře | Testovací soubor | Typ povrchu | Chráněný prvek a kontext | Výsledek |
|---|---|---|---|---|
| `neg_01_uni_prerekvizity` | `clean_uni_syllabus.json` | `app` | Termín *Prerekvizity* v univerzitním IS zůstal zachován; ICU proměnné `{credits}` a `{courseCode}` netknuty. | ✅ PASS (0 blokátorů) |
| `neg_02_hr_hygienicke_faktory` | `clean_hr_slides.md` | `slides` | Odborný termín *Hygienické faktory* z Herzbergovy teorie motivace v HR slidu zachován; heslovitý Profil A bez teček uznán jako správný. | ✅ PASS (0 blokátorů) |
| `neg_03_tech_robustni_sifrovani` | `clean_tech_specs.json` | `app` | Termín *robustní šifrování AES-256* zachován, protože je podložen konkrétním mechanismem. | ✅ PASS (0 blokátorů) |
| `neg_04_clean_checkout` | `clean_checkout_app.json` | `app` | Vzorový český košík s dokonavými infinitivy a heselným výčtem vrátil explicitní verdikt `BEZ ÚPRAV`. | ✅ PASS (`BEZ ÚPRAV`) |
| `neg_05_clean_faq` | `clean_faq_web.md` | `web` | Syntakticky navázaný výčet s malými písmeny, středníky a závěrečnou tečkou uznán jako platný Profil B ÚJČ. | ✅ PASS (0 blokátorů) |

### Koš C: Hraniční stavy a i18n
Cílem je ověřit robustnost při zpracování kódu, složité syntaxe a dodržení limitu záběru:

| ID scénáře | Testovací soubor | Typ povrchu | Hraniční podmínka | Výsledek |
|---|---|---|---|---|
| `edge_01_i18n_icu` | `boundary_i18n_icu.json` | `app` | Složitý ICU plurál `{count, plural, ...}` i HTML značky `<strong>` zůstaly 100% zachovány. | ✅ PASS |
| `edge_02_mixed_tone` | `boundary_mixed_tone.json` | `app` | Úspěšně odhalen rozpor mezi tykáním a vykáním v rámci jedné obrazovky. | ✅ PASS |
| `edge_03_network_drop` | `boundary_network_drop.json` | `app` | Odmítnutí slepé výzvy k opakování platby při timeoutu spojení; ochrana proti vícenásobné platbě. | ✅ PASS |
| `edge_04_out_of_scope_blog` | `out_of_scope_blog.md` | `none` | 800slovný článek: tvrdé odmítnutí plného přepisu; nabídnuta pouze kontrola nadpisů a CTA. | ✅ PASS (odmítnuto) |

---

## 4. Spuštění a reprodukce benchmarku

Všechny testy a benchmarky lze kdykoli lokálně reprodukovat spuštěním jediného příkazu bez externích závislostí:

```bash
# 1. Běh jednotkových testů linteru (19 testů)
python3 -m unittest discover tests

# 2. Běh kompletní evaluační a benchmarkovací sady (15 scénářů + 24 aktivačních dotazů)
python3 scripts/run_evals.py
```
