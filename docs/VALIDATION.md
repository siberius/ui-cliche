# Ověření a validace / Validation

Copyright © 2026 Luděk Sušický

## Stav / Status

Verze / Version: **ui-cliche 2.0.0** (2026-11-22)

Česky: Verze 2.0.0 disponuje kompletní čtyřvrstvou evaluační architekturou. Kvalita byla exaktně změřena na zlaté sadě 15 behaviorálních scénářů rozdělených do tří testovacích košů (Koš A – pozitivní vady, Koš B – negativní korpus čistých lidských textů pro měření FPR, Koš C – hraniční stavy a ochrana i18n proměnných) a na sadě 24 dotazů pro přesnost spuštění. Kompletní výsledky a naměřené hodnoty naleznete v [docs/BENCHMARK.md](BENCHMARK.md) a strojovém reportu [evals/benchmark.json](../evals/benchmark.json).

English: Version 2.0.0 features a full four-layer evaluation suite. Empirical quality was verified across a golden suite of 15 behavioral scenarios across three baskets (Basket A: positive flaws, Basket B: true negative human texts measuring FPR, Basket C: edge cases and i18n syntax protection) and 24 activation trigger queries. Full results are documented in [docs/BENCHMARK.md](BENCHMARK.md) and [evals/benchmark.json](../evals/benchmark.json).

---

## Přehled evaluačních vrstev

| Vrstva | Soubor | Obsah a rozsah | Dosažený výsledek (v2.0) |
|---|---|---|---|
| **1. Testy spuštění** | `evals/trigger_evals.json` | 24 českých dotazů (12 v záběru, 12 mimo záběr). | **100,0 % přesnost** (všechny dotazy správně klasifikovány). |
| **2. Unit testy linteru** | `tests/test_ui_lint.py` | 19 deterministických testů (povinný pozitivní vzor + protipříklad). | **19/19 testů úspěšných** (~0.003 s). |
| **3. Zlatý korpus** | `evals/evals.json` | 15 scénářů s deterministickými a LLM asercemi (`evals/corpus/`). | **100,0 % záchyt** (Koš A), **0,0 % FPR** (Koš B), **100,0 % i18n** (Koš C). |
| **4. Reprodukovatelný běh** | `scripts/run_evals.py` | CLI spouštěč generující souhrnné metriky do `evals/benchmark.json`. | Plně automatizováno. |

---

## Kontrolní scénáře zlatého korpusu

| ID | Vstupní scénář | Koš | Očekávaný výsledek | Naměřeno |
|---|---|---|---|---|
| `pos_01_saas_landing` | `messy_saas_landing.html` | Koš A | Záchyt Title Case, odhalení superlativů bez důkazu. | ✅ PASS |
| `pos_02_modal_imperative` | `messy_modal_imperative.json` | Koš A | Záchyt teček za tlačítky, oprava imperativu, záchyt „Upsík“. | ✅ PASS |
| `pos_03_slides_bullets` | `messy_slides_bullets.md` | Koš A | Záchyt smíšených odrážek, triáž prerekvizit a mrtvých adres. | ✅ PASS |
| `pos_04_bad_link_texts` | `messy_links.json` | Koš A | Odhalení generických odkazů „Více“ a „Klikněte zde“. | ✅ PASS |
| `pos_05_unverified_cta` | `messy_cta_commitments.json` | Koš A | Odhalení klamavého závazku „ihned zdarma“ se štítkem `[ověřit obchodní podmínku]`. | ✅ PASS |
| `pos_06_em_dashes` | `messy_typography_dashes.md` | Koš A | Záchyt všech dlouhých pomlček (—) s náhradou za krátkou (–). | ✅ PASS |
| `neg_01_uni_prerekvizity` | `clean_uni_syllabus.json` | Koš B | Termín „Prerekvizity“ v univerzitním IS zachován, 0 blokátorů. | ✅ PASS |
| `neg_02_hr_hygienicke_faktory` | `clean_hr_slides.md` | Koš B | Herzbergovy „Hygienické faktory“ zachovány, Profil A uznán. | ✅ PASS |
| `neg_03_tech_robustni_sifrovani`| `clean_tech_specs.json` | Koš B | Doložené „robustní šifrování AES-256“ zachováno, 0 blokátorů. | ✅ PASS |
| `neg_04_clean_checkout` | `clean_checkout_app.json` | Koš B | Vzorový košík vrátil explicitní verdikt `BEZ ÚPRAV`. | ✅ PASS |
| `neg_05_clean_faq` | `clean_faq_web.md` | Koš B | Syntakticky navázaný výčet ÚJČ (Profil B) uznán bez vad. | ✅ PASS |
| `edge_01_i18n_icu` | `boundary_i18n_icu.json` | Koš C | ICU proměnné `{count, plural, ...}` i HTML značky 100% zachovány. | ✅ PASS |
| `edge_02_mixed_tone` | `boundary_mixed_tone.json` | Koš C | Odhalen rozpor mezi tykáním a vykáním na obrazovce. | ✅ PASS |
| `edge_03_network_drop` | `boundary_network_drop.json` | Koš C | Zákaz slepé výzvy k opakování po timeoutu platby. | ✅ PASS |
| `edge_04_out_of_scope_blog` | `out_of_scope_blog.md` | Koš C | 800slovný článek: plný přepis odmítnut, dodržen limit. | ✅ PASS |
