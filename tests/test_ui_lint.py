#!/usr/bin/env python3
"""
test_ui_lint.py - Jednotkové testy deterministického linteru ui_lint.py.

Autor: Luděk Sušický (MIT License)
Metodická inspirace:
  - Zásada povinné dvojice pozitivní vzor + protipříklad pro každé pravidlo
    po vzoru regresního testování projektu kalky (Zdeněk Dvořák, MIT).
Testovací sada, scénáře a verifikační logika:
  Původní autorský kód pro projekt ui-cliche v2.0.
"""

import os
import sys
import unittest

# Přidání scripts do sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts")))
from ui_lint import lint_content, load_keep_terms, TextMasker


class TestUILintMasker(unittest.TestCase):
    """Testy maskování proměnných a značek."""

    def setUp(self):
        self.masker = TextMasker()

    def test_mask_icu_and_html(self):
        text = "Zbývá vám {count} kreditů pro uživatele {{user}} v <strong>systému</strong>."
        masked = self.masker.mask(text)
        self.assertNotIn("{count}", masked)
        self.assertNotIn("{{user}}", masked)
        self.assertNotIn("<strong>", masked)
        self.assertIn("__PH_0__", masked)

        unmasked = self.masker.unmask(masked)
        self.assertEqual(unmasked, text)


class TestHardLintRules(unittest.TestCase):
    """Testy tvrdých deterministických vad (hard_lint)."""

    def test_em_dash_positive(self):
        """Pozitivní test: em-dash (—) musí být zachycen."""
        text = "Export dat — dokončeno úspěšně."
        hard, soft, _ = lint_content(text, surface="app", keep_terms=set())
        rule_ids = [h["rule_id"] for h in hard]
        self.assertIn("TYPO_EM_DASH", rule_ids)

    def test_em_dash_counter_example(self):
        """Protipříklad: česká krátká pomlčka (–) nesmí vyvolat chybu."""
        text = "Export dat – dokončeno úspěšně."
        hard, soft, _ = lint_content(text, surface="app", keep_terms=set())
        rule_ids = [h["rule_id"] for h in hard]
        self.assertNotIn("TYPO_EM_DASH", rule_ids)

    def test_button_period_positive(self):
        """Pozitivní test: tečka za krátkým tlačítkem musí být zachycena."""
        text = "Uložit změny."
        hard, soft, _ = lint_content(text, surface="app", keep_terms=set())
        rule_ids = [h["rule_id"] for h in hard]
        self.assertIn("UI_BUTTON_PERIOD", rule_ids)

    def test_button_period_counter_example_clean_button(self):
        """Protipříklad: tlačítko bez tečky projde."""
        text = "Uložit změny"
        hard, soft, _ = lint_content(text, surface="app", keep_terms=set())
        rule_ids = [h["rule_id"] for h in hard]
        self.assertNotIn("UI_BUTTON_PERIOD", rule_ids)

    def test_button_period_counter_example_ellipsis(self):
        """Protipříklad: výpustek (trojtečka) na tlačítku projde."""
        text = "Načítám další…"
        hard, soft, _ = lint_content(text, surface="app", keep_terms=set())
        rule_ids = [h["rule_id"] for h in hard]
        self.assertNotIn("UI_BUTTON_PERIOD", rule_ids)

    def test_button_period_counter_example_explanatory_sentence(self):
        """Protipříklad: celovětná vysvětlující hláška v app tečku mít smí."""
        text = "Při smazání projektu budou nevratně odstraněna všechna přiřazená data."
        hard, soft, _ = lint_content(text, surface="app", keep_terms=set())
        rule_ids = [h["rule_id"] for h in hard]
        self.assertNotIn("UI_BUTTON_PERIOD", rule_ids)

    def test_title_case_positive(self):
        """Pozitivní test: anglická kapitalizace českých slov v nadpisu."""
        text = "Správa Uživatelských Účtů"
        hard, soft, _ = lint_content(text, surface="web", keep_terms=set())
        rule_ids = [h["rule_id"] for h in hard]
        self.assertIn("TYPO_TITLE_CASE", rule_ids)

    def test_title_case_counter_example_sentence_case(self):
        """Protipříklad: správná česká kapitalizace (pouze první slovo velké)."""
        text = "Správa uživatelských účtů"
        hard, soft, _ = lint_content(text, surface="web", keep_terms=set())
        rule_ids = [h["rule_id"] for h in hard]
        self.assertNotIn("TYPO_TITLE_CASE", rule_ids)

    def test_title_case_counter_example_whitelist_proper_nouns(self):
        """Protipříklad: oficiální vlastní jména z whitelistu projdou."""
        text = "Česká republika v Evropské unii"
        hard, soft, _ = lint_content(text, surface="web", keep_terms=set())
        rule_ids = [h["rule_id"] for h in hard]
        self.assertNotIn("TYPO_TITLE_CASE", rule_ids)

    def test_ai_filler_positive(self):
        """Pozitivní test: generické klišé odkašlání."""
        text = "V dnešní uspěchané době je správa hesel klíčová."
        hard, soft, _ = lint_content(text, surface="web", keep_terms=set())
        rule_ids = [h["rule_id"] for h in hard]
        self.assertIn("AI_FILLER_INTRO", rule_ids)

    def test_ai_filler_counter_example(self):
        """Protipříklad: přímé věcné sdělení."""
        text = "Správce hesel šifruje vaše přihlašovací údaje."
        hard, soft, _ = lint_content(text, surface="web", keep_terms=set())
        rule_ids = [h["rule_id"] for h in hard]
        self.assertNotIn("AI_FILLER_INTRO", rule_ids)

    def test_list_mixed_punctuation_positive(self):
        """Pozitivní test: smíšený výčet (jedna položka s tečkou, druhá bez)."""
        lines = [
            "- Export do formátu PDF.",
            "- Uložení na lokální disk",
        ]
        text = "\n".join(lines)
        hard, soft, _ = lint_content(text, surface="slides", keep_terms=set())
        rule_ids = [h["rule_id"] for h in hard]
        self.assertIn("LIST_MIXED_PUNCTUATION", rule_ids)

    def test_list_mixed_punctuation_counter_example_profile_a(self):
        """Protipříklad: čistý heslovitý Profil A (žádná tečka)."""
        lines = [
            "- Export do formátu PDF",
            "- Uložení na lokální disk",
            "- Odeslání e-mailem",
        ]
        text = "\n".join(lines)
        hard, soft, _ = lint_content(text, surface="slides", keep_terms=set())
        rule_ids = [h["rule_id"] for h in hard]
        self.assertNotIn("LIST_MIXED_PUNCTUATION", rule_ids)

    def test_list_mixed_punctuation_counter_example_profile_b(self):
        """Protipříklad: čistý syntakticky navázaný Profil B (čárky + závěrečná tečka)."""
        lines = [
            "- export do formátu PDF,",
            "- uložení na lokální disk,",
            "- odeslání e-mailem.",
        ]
        text = "\n".join(lines)
        hard, soft, _ = lint_content(text, surface="web", keep_terms=set())
        rule_ids = [h["rule_id"] for h in hard]
        self.assertNotIn("LIST_MIXED_PUNCTUATION", rule_ids)

    def test_list_mixed_punctuation_counter_example_profile_c(self):
        """Protipříklad: čistý větný Profil C (vše s tečkou)."""
        lines = [
            "- Exportujeme data do formátu PDF.",
            "- Ukládáme kopii na lokální disk.",
            "- Odesíláme souhrnný e-mail.",
        ]
        text = "\n".join(lines)
        hard, soft, _ = lint_content(text, surface="slides", keep_terms=set())
        rule_ids = [h["rule_id"] for h in hard]
        self.assertNotIn("LIST_MIXED_PUNCTUATION", rule_ids)


class TestSoftCandidateRules(unittest.TestCase):
    """Testy měkkých kandidátů a podpory keep-terms."""

    def test_soft_candidate_prerekvizity(self):
        """Kandidát prerekvizity se označí pro LLM adjudikaci."""
        text = "Předměty a jejich prerekvizity pro zimní semestr."
        hard, soft, _ = lint_content(text, surface="app", keep_terms=set())
        self.assertEqual(len(hard), 0)
        self.assertTrue(any(s["term"].startswith("prerekvizit") for s in soft))

    def test_soft_candidate_keep_terms_bypass(self):
        """Pokud je termín v keep_terms, linter ho neoznačí."""
        text = "Předměty a jejich prerekvizity pro zimní semestr."
        keep_terms = {"prerekvizity", "prerekvizit"}
        hard, soft, _ = lint_content(text, surface="app", keep_terms=keep_terms)
        self.assertEqual(len(hard), 0)
        self.assertFalse(any(s["term"].startswith("prerekvizit") for s in soft))

    def test_soft_candidate_hygienicky_standard(self):
        """Kandidát hygienický standard se označí k triáži."""
        text = "Bezpečnost dat je náš hygienický standard."
        hard, soft, _ = lint_content(text, surface="web", keep_terms=set())
        self.assertTrue(any("hygienick" in s["term"] for s in soft))


if __name__ == "__main__":
    unittest.main()
