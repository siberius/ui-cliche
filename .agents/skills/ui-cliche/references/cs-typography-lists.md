# Česká typografie a interpunkce výčtů (cs-typography-lists)

Copyright © 2026 Luděk Sušický (MIT License)

> **Normativní autority a zdroje:**  
> - Pravidla pro psaní výčtů, uvozovek a vynechávání teček u titulků: *Ústav pro jazyk český AV ČR (ÚJČ AV ČR)*.  
> - Typografická úprava čísel, pomlček a značek: *ČSN 01 6910*.  
> - Formulace čtyř profilů výčtů A–D pro digitální aplikace a slidy: původní autorská specifikace pro projekt `ui-cliche v2.0`.

Závazná referenční pravidla podle norem ÚJČ AV ČR a ČSN 01 6910 pro rozhraní aplikací, webové stránky a prezentace.

---

## 1. Čtyři interpunkční profily položek seznamů (Výčty)

Základní pravidlo: **Styly se v rámci jednoho seznamu nikdy nemíchají!**

### Profil A – Heslovitý výčet (výchozí pro aplikace, tabulky a stručné slidy)
- **Charakteristika:** Položky mají nevětnou povahu, tvoří samostatná hesla nebo volby a jsou graficky zřetelně odděleny (odrážky, karty, zaškrtávací pole).
- **Uvozovací věta:** Může být bez dvojtečky, nebo s orientační dvojtečkou.
- **Písmeno na začátku:** V UI začínají položky velkým písmenem (v textových výčtech je přípustné i jednotné malé).
- **Zakončení položek:** **ŽÁDNÁ TEČKA ANI ČÁRKA.**
- **Příklad v rozhraní:**
  - Exportovat do formátu PDF
  - Uložit záložní kopii na disk
  - Odeslat souhrnný report e-mailem

### Profil B – Syntakticky navázaný nevětný výčet (weby, FAQ, vysvětlivky)
- **Charakteristika:** Položky plynule navazují na uvozovací větu a tvoří s ní jediný syntaktický celek.
- **Uvozovací věta:** **Povinně končí dvojtečkou (`:`).**
- **Písmeno na začátku:** Malé písmeno u všech položek.
- **Zakončení položek:** Položky se oddělují čárkou (`,`), jsou-li delší nebo obsahují-li vnitřní čárky, pak středníkem (`;`).
- **Zakončení poslední položky:** **Povinně tečka (`.`).**
- **Příklad:**
  Balíček Professional obsahuje:
  - neomezený počet odeslaných faktur,
  - automatické párování bankovních pohybů,
  - telefonickou technickou podporu v pracovní dny.

### Profil C – Větný výčet (onboarding, argumentační slidy, kroky procesu)
- **Charakteristika:** Každá položka tvoří samostatnou, gramaticky úplnou větu.
- **Uvozovací věta:** Může končit dvojtečkou nebo tečkou.
- **Písmeno na začátku:** Velké písmeno u každé položky.
- **Zakončení položek:** **Plná větná interpunkce** – tečka (`.`), případně otazník (`?`) nebo vykřičník (`!`).
- **Příklad:**
  Postup nastavení účtu:
  - Zadejte svou e-mailovou adresu a zvolte si bezpečné heslo.
  - Otevřete potvrzovací odkaz, který jsme vám právě odeslali do schránky.
  - Vyberte si platební metodu pro aktivaci předplatného.

### Profil D – Normalizace smíšených výčtů
- Pokud strojový text míchá větné body s hesly, **nejprve navrhněte syntaktické sjednocení**:
  - buď na heslovitý Profil A (zkrácení na věcná hesla bez teček),
  - nebo na větný Profil C (doplnění podnětu a přísudku do celých vět s tečkami).
- Pokud uživatel trvá na zachování smíšeného obsahu, uplatní se pravidlo ÚJČ: malé písmeno na začátku, oddělení středníky a závěrečná tečka.

---

## 2. Pravidla mikrotypografie v češtině

### Zákaz koncové tečky u nadpisů a tlačítek
- Samostatné nadpisy všech úrovní (H1 až H6), popisky formulářových polí (Labels) a tlačítka **nikdy nekončí tečkou**.
- Pokud má popisek pod polem dvě celé věty, tečka se píše uvnitř mezi větami i na konci vysvětlujícího odstavce, ale samotný titulek nad polem zůstává bez tečky.

### Pomlčky a spojovníky
- **Spojovník (`-`):** Pouze pro těsná složená slova (*česko-anglický*, *e-mail*). Nikdy s mezerami.
- **Dlouhá pomlčka (em-dash `—`):** **ZÁKAZ v české sazbě.** Typický pozůstatek anglických textů.
- **Krátká pomlčka (en-dash `–`):** Správná česká pomlčka pro oddělení větných celků (*Všechny změny – včetně historie – jsou uloženy.*) a pro rozsahy bez mezer (*10–15 minut*, *strany 20–25*).

### České uvozovky
- V souvislém českém textu se používají výhradně uvozovky dole a nahoře: **„uvozovky“** (kód 99 dole, 66 nahoře).
- Rovné uvozovky (`"` a `'`) jsou vyhrazeny pouze pro syntaxi kódu, HTML a JSON.

### Mezery u čísel, jednotek a procent
- **Procenta:**
  - `15 %` (s mezerou) = podstatné jméno *„patnáct procent“*.
  - `15%` (bez mezery) = přídavné jméno *„patnáctiprocentní“* (*15% sleva*).
- **Měna a jednotky:** Vždy s nezlomitelnou mezerou (*250 Kč*, *5 kg*, *100 m*).
- **Velká čísla:** Čtyř- a vícemístná čísla mimo letopočty se člení mezerou po třech řádech (*10 000 uživatelů*, *1 250 000 Kč*).
