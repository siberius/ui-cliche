# Povrch: Aplikace a digitální produkty (App UI)

Referenční pravidla pro české texty v uživatelských rozhraních, formulářích a lokalizačních souborech (vychází z Mozilla L10n CS a české UX praxe).

## 1. Tlačítka a primární akce
- **Výhradně dokonavý infinitiv:** Tlačítko pojmenovává výsledek nebo dokončení akce.
  - ✅ *Uložit*, *Odeslat objednávku*, *Nainstalovat*, *Vytvořit projekt*, *Pokračovat*.
  - ❌ Nikdy rozkazovací způsob (imperativ): *Ulož*, *Nainstaluj*, *Klikni*, *Odešli*.
  - ❌ Nikdy nedokonavý tvar, pokud nejde o probíhající proces: *Ukládat*.
- **Upřesnění závazku:** Pokud akce není okamžitá nebo nevratná, upřesněte sloveso:
  - *Odeslat žádost o rezervaci* (místo klamavého *Rezervovat*).
  - *Uložit koncept* (místo obecného *Uložit*).
- **Bez koncové tečky:** Samostatné tlačítko nesmí končit tečkou (*Uložit změny*, nikoli *Uložit změny.*). Výpustek se píše pouze v případě, že akce bezprostředně vyžaduje další krok / dialog (*Vybrat soubor…*).

## 2. Tooltipy a nápovědy
- **Činný rod se zamlčeným podmětem:** Samotný prvek rozhraní vykonává akci.
  - ✅ *„Zobrazí historii změn“*, *„Otevře nabídku exportu“*, *„Zkopíruje odkaz do schránky“*.
  - ❌ Pasivum nebo imperativ: *„Zde můžete vidět historii“*, *„Kliknutím zobrazíte historii“*, *„Historie změn je zobrazena“*.

## 3. Odkazy a navigace
- **Odkaz nese název cíle:** Uživatel i čtečka obrazovky musí vědět, kam odkaz vede, bez čtení okolního textu.
  - ✅ *„Podmínky vrácení zboží“*, *„Zásady ochrany osobních údajů“*, *„Dokumentace k API“*.
  - ❌ Obecné výzvy: *„Více“*, *„Zde“*, *„Klikněte zde“*, *„Zjistit více“*.

## 4. Oddělení popisku, nápovědy a placeholderu
- **Popisek (Label):** Trvale viditelný nad polem (*E-mailová adresa*).
- **Placeholder:** Slouží výhradně jako formátový vzor (*např. jan.novak@firma.cz*), nikoli jako instrukce nebo náhrada popisku.
- **Nápověda (Helper text):** Umístěna pod polem pro upřesnění formátu nebo omezení (*Minimálně 8 znaků včetně číslice*).

## 5. Audit šesti stavů rozhraní
Při kontrole formuláře nebo interaktivního bloku ověřte přítomnost a tón všech 6 stavů:
1. **Výchozí stav (Default):** Přehledná pole, jasné výchozí hodnoty.
2. **Průběh (Loading/Progress):** Nedokonavý tvar nebo podstatné jméno slovesné (*Odesílám platbu…*, *Ukládání změn…*).
3. **Chyba pole (Field validation):** Konkrétní věcné vysvětlení, jak chybu napravit (*Zadejte platnou e-mailovou adresu ve formátu jmeno@domena.cz*).
4. **Chyba serveru (System error):** Věcný popis bez interních kódů a bez zlehčování (*Platbu se nepodařilo zpracovat. Vaše karta nebyla zatížena. Zkuste to prosím znovu.*).
   - ❌ Zákaz křečovitého humoru: *„Upsík, spadlo nám to pod stůl“*, *„Jejda, něco se pokazilo“*.
5. **Výpadek spojení / nejistý stav (Network drop):** Pokud systém neví, zda akce proběhla (např. timeout platby), nesmí slepě vyzvat k novému odeslání.
   - ✅ *„Ověřujeme stav vaší platby u banky. Neodesílejte formulář znovu, abyste předešli vícenásobnému stržení částky.“*
6. **Úspěch (Success):** Jasné potvrzení přijetí a další krok (*Objednávku číslo 2026-081 jsme v pořádku přijali. Potvrzení jsme odeslali na váš e-mail.*).

## 6. Konzistence oslovení (Tykání vs. Vykání)
- Striktně držte jednu linii v celém rozhraní:
  - Buď vykání (*Zadejte své heslo*, *Váš účet*),
  - nebo tykání (*Zadej své heslo*, *Tvůj profil*).
- Nikdy nemíchejte obě formy na jedné obrazovce ani v jednom toku!

## 7. Ochrana i18n proměnných
- Všechny zástupné znaky ICU (`{count}`, `{name}`), printf (`%s`, `%d`), šablon (`{{user}}`) a HTML značky (`<strong>`, `<br/>`) musí zůstat beze změny!
