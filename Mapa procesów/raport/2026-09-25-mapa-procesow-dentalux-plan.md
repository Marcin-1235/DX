# Mapa procesów Dentalux: plan krok po kroku

*Data: 2026-09-25 · Autor: Claude Code na zlecenie Marcina Kasiaka*
*Źródła: publiczne informacje o Dentalux (dentalux.pl, ZnanyLekarz), wytyczne NHS i IHI dotyczące mapowania procesów, literatura o metodzie lean w ochronie zdrowia oraz polskie przepisy. Linki są na końcu dokumentu.*

---

## 0. TL;DR (streszczenie na jednej stronie)

1. **Zacznij od celu, nie od rysowania.** Najpierw ustal, po co powstaje mapa: standaryzacja dwóch klinik, wdrożenie systemu IT lub AI, skrócenie czasu do pierwszej wizyty czy przygotowanie do kontroli. Od celu zależy poziom szczegółowości i kolejność prac.
2. **Zrób najpierw mapę ogólną (poziom 0–1), potem szczegóły.** Na start wystarczy jedna strona A3 ze wszystkimi procesami Dentalux. Szczegółowe diagramy z torami (swimlane) rób tylko dla 5–7 procesów o największym znaczeniu.
3. **Obserwuj, a nie tylko pytaj.** To, co ludzie mówią o swojej pracy, zawsze różni się od tego, co faktycznie robią. Zakładaj z góry, że znajdziesz obejścia, karteczki na monitorach, „zeszyt pani Basi” i prywatne grupy na WhatsAppie.
4. **Narzędzia:** na warsztaty karteczki samoprzylepne i szary papier, do porządkowania SIPOC, do dokumentacji diagramy z torami w draw.io lub Miro. BPMN tylko wtedy, gdy proces będzie automatyzowany.
5. **Kolejność procesów:** ścieżka pacjenta, czyli od pierwszego kontaktu do przypomnienia o wizycie kontrolnej, i przede wszystkim plan leczenia. Potem procesy krytyczne dla bezpieczeństwa i zgodności z prawem (sterylizacja, RTG i CBCT, dokumentacja, zgody). Na końcu procesy wspierające i zarządcze.
6. **Najwięcej problemów powstaje na styku procesów,** w momentach przekazania pracy między osobami: rejestracja → asysta → lekarz → pracownia protetyczna → rejestracja. Właśnie tam mapuj najdokładniej.
7. **Czas:** około 8–10 tygodni przy pracy części etatu. Pierwszy namacalny efekt, czyli mapa ogólna i diagnoza ścieżki pacjenta, jest możliwy po 3–4 tygodniach.

---

## 1. Co wiemy o Dentalux i co z tego wynika dla mapowania

| Fakt (źródło publiczne) | Konsekwencja dla mapy procesów |
|---|---|
| **2 kliniki na Mokotowie:** Racławicka 131 (7 dni w tygodniu, 8–21, także w święta) i Puławska 257 (pon.–pt., 8–21) | Mapuj **obie** kliniki osobno i porównaj je. Różnice to materiał do standaryzacji. W weekendy działa tylko Racławicka, więc powstają osobne scenariusze: pacjent z Puławskiej przychodzi w sobotę, a dokumentacja, plan leczenia i sprzęt muszą być dostępne w drugiej klinice. |
| **Od 1994 r., ponad 100 tys. pacjentów, ponad 35 lekarzy** | Firma działa ponad 30 lat, więc ma dużo **wiedzy niepisanej** i nawyków („zawsze tak robiliśmy”). Lekarze prawdopodobnie pracują częściowo na umowach B2B, a wtedy procesy „należą” do lekarza, a nie do firmy (patrz §8). |
| **Szeroki zakres specjalizacji:** zachowawcza, endodoncja z mikroskopem, implanty, ortodoncja (w tym Invisalign), protetyka, periodontologia, chirurgia (laser), pedodoncja, higiena, estetyka (DSD) | Ścieżki są długie, obejmują kilka specjalności i wiele wizyt, a leczenie implantologiczno-protetyczne trwa miesiącami. Kluczowe są **plan leczenia kompleksowego** i **koordynacja między specjalistami**. |
| **CBCT, RTG, radiowizjografia** | Aparat CBCT to **wspólny zasób**, który może być wąskim gardłem. Na mapie jest też osobna ścieżka ochrony radiologicznej (patrz §7). |
| **Znieczulenie ogólne** | To osobna ścieżka wysokiego ryzyka: kwalifikacja, anestezjolog, zgody, pacjent na czczo, wybudzenie, wypis. Wymaga dokładnej mapy. |
| **Rejestracja:** telefon, formularz www, e-mail osobny dla każdej kliniki, ZnanyLekarz | Co najmniej **4 kanały wejścia pacjenta**. Trzeba sprawdzić, czy wszystkie trafiają do jednego grafiku, kto odpisuje na e-maile i jak szybko, i czy występują podwójne rezerwacje. |
| **Wyłącznie prywatnie (brak umowy z NFZ)**, raty MediRaty, karta rabatowa | Proces finansowy obejmuje wycenę planu leczenia, akceptację, raty (weryfikację zewnętrzną), rabaty, zaliczki i rozliczenie prac protetycznych. Akceptacja planu leczenia to kluczowy wskaźnik biznesowy. |
| **Brak informacji o własnej pracowni protetycznej** | **Do sprawdzenia w pierwszym tygodniu.** Zewnętrzna pracownia to kluczowy punkt przekazania: wycisk lub skan → kurier → termin → przymiarka → poprawki. |
| Nagroda Orły Medycyny 2026, 5/5 na ZnanyLekarz (26 opinii) | Klienci wysoko oceniają obsługę. Mapa powinna chronić to, co działa, a nie tylko szukać błędów. |

> ⚠️ Informacje pochodzą ze strony www i portali. Nie znam wewnętrznego oprogramowania Dentalux (np. Estomed, Mediporta, Dentoma, Clinic Solution, Medfile), stanu zatrudnienia asyst, higienistek i rejestracji ani modelu współpracy z lekarzami. **To pierwsze rzeczy do ustalenia.**

---

## 2. Narzędzia: co, kiedy i dlaczego

### 2.1 Analogowe (nie lekceważ ich)

| Narzędzie | Kiedy | Uwagi |
|---|---|---|
| **Kartka A4 i długopis** | Obserwacja w terenie, notatki z wywiadów, szybkie szkice | Najlepsze narzędzie do obserwacji. Nie odciąga uwagi, nie budzi nieufności jak laptop i nie zapisuje danych pacjentów w chmurze. |
| **Szary papier i karteczki samoprzylepne** | Warsztaty z zespołem, mapa „jak jest” (as-is) | Każdy może przykleić, przestawić albo dopisać swoją karteczkę. Stosuj **kody kolorów**: żółty = czynność, różowy = problem lub strata, zielony = pomysł, niebieski = dokument lub system IT, pomarańczowy = decyzja. Na koniec zrób zdjęcie telefonem i przepisz mapę cyfrowo. |
| **Rzut kliniki A3 i kolorowe mazaki** | Diagram spaghetti (ruch ludzi i narzędzi) | Śledź np. asystę przez 1 godzinę: gabinet → sterylizacja → magazyn → RTG → recepcja. Często wychodzi kilometr dziennie zbędnego chodzenia. |
| **Stoper (telefon)** | Pomiar czasów | Czas oczekiwania w poczekalni, przygotowanie gabinetu między pacjentami, czas rozmowy telefonicznej, cykl sterylizacji. |
| **Tablica korkowa lub ściana w pokoju socjalnym** | Wystawienie mapy na 1–2 tygodnie | Ludzie sami dopisują uwagi. To najtańsza metoda weryfikacji mapy. |

### 2.2 Metody i notacje

| Metoda | Do czego | Kiedy w projekcie |
|---|---|---|
| **SIPOC** (dostawcy → wejścia → proces → wyjścia → odbiorcy) | Wyznaczenie granic procesu: gdzie się zaczyna i kończy, kto dostarcza, kto odbiera | Tydzień 1–2, dla każdego procesu z listy |
| **Mapa procesów (poziom 0)** | Jedna strona pokazująca wszystkie procesy i ich podział: podstawowe, wspierające, zarządcze | Tydzień 1–2 |
| **Diagram z torami (swimlane)** | Główne narzędzie. Każda rola ma swój tor (pacjent, rejestracja, asysta, lekarz, higienistka, pracownia, księgowość), więc od razu widać przekazania | Tydzień 3–6 |
| **Mapa ścieżki pacjenta (patient journey)** | Perspektywa pacjenta: co widzi, co czuje, gdzie czeka, gdzie się denerwuje | Równolegle z diagramami z torami |
| **Mapa strumienia wartości (VSM)** | Czas całkowity a czas, który daje pacjentowi wartość. Pokazuje oczekiwanie i straty | Dla 1–2 kluczowych ścieżek, np. pierwsza wizyta → plan leczenia |
| **Diagram spaghetti** | Ruch fizyczny | Sterylizacja, magazyn, CBCT |
| **RACI** (kto wykonuje, kto odpowiada, kogo pytamy, kogo informujemy) | Odpowiedzialności | Po mapie „jak jest”, przed mapą „jak ma być” |
| **Diagram Ishikawy lub 5 × Dlaczego** | Przyczyny źródłowe problemów wskazanych na mapie | Faza analizy |
| **BPMN 2.0** | Formalna notacja, gdy proces ma trafić do systemu lub automatyzacji (np. przypomnienia, recall, obieg zgód) | Dopiero w fazie „jak ma być” i tylko dla procesów do automatyzacji |

### 2.3 Cyfrowe

- **draw.io (diagrams.net):** darmowe, działa offline, pliki można trzymać w repozytorium lub na Google Drive. **Rekomendowane jako główne repozytorium map.**
- **Miro lub Mural:** warsztaty hybrydowe (dwie kliniki, lekarze z różnymi grafikami), zbieranie komentarzy asynchronicznie.
- **Lucidchart:** jak draw.io, ale płatne. Ma lepsze funkcje współpracy.
- **Bizagi Modeler lub Camunda Modeler:** darmowe narzędzia BPMN. Użyj ich dopiero wtedy, gdy będziesz projektować automatyzację.
- **Signavio, ARIS:** poziom korporacyjny, dla dwóch klinik to przesada.
- **Arkusz (Google Sheets lub Excel):** rejestr procesów z kolumnami: ID, nazwa, właściciel, SIPOC, wskaźniki, ryzyka, status mapy, link do diagramu.
- **Claude lub inny model AI:** transkrypcja i porządkowanie notatek z wywiadów, zamiana zdjęć karteczek na listy kroków, pierwsze wersje SIPOC. **Nigdy nie wprowadzaj danych pacjentów** (patrz §8.3).

**Rekomendacja:** papier do pracy w terenie i na warsztatach, draw.io do dokumentacji, arkusz jako rejestr, Miro tylko przy pracy zdalnej. Nie kupuj narzędzia BPM, zanim nie wiesz, co będziesz automatyzować.

---

## 3. Plan krok po kroku

### Faza 0: Przygotowanie (tydzień 0–1)

1. **Ustal cel ze sponsorem (zarząd).** Zadaj trzy pytania: *Po co to robimy? Co ma się zmienić za 6 miesięcy? Po czym poznamy sukces?* Przykładowe cele: ujednolicenie standardu obu klinik, wybór i wdrożenie nowego systemu, zwiększenie akceptacji planów leczenia, przygotowanie do akredytacji lub kontroli, zmniejszenie obciążenia rejestracji dzięki automatyzacji i AI.
2. **Ustal zakres i granice.** Na przykład: „wszystkie procesy obu klinik, bez księgowości zewnętrznej”.
3. **Wyznacz sponsora** (osobę, która ma władzę rozstrzygać spory) oraz **zespół roboczy**: kierownika rejestracji, asystę lub higienistkę, 1–2 lekarzy (w tym jednego „sceptyka”), osobę od sterylizacji, osobę od finansów lub rozliczeń, a jeśli jest, osobę odpowiedzialną za IT lub RODO.
4. **Poinformuj cały zespół** (mailem i na odprawie): *to nie jest kontrola ani ocena ludzi, mapujemy procesy, a nie osoby*. To najważniejsza pojedyncza czynność zmniejszająca opór.
5. **Zbierz istniejące dokumenty:** procedury sanitarno-higieniczne, procedury sterylizacji, dokumentację ochrony radiologicznej, regulamin organizacyjny, wzory zgód, cennik, instrukcje systemu, grafik, umowy z pracowniami i firmą od odpadów. Nie traktuj ich jak prawdy, tylko jako zapis tego, jak **powinno** być.
6. **Uzyskaj dostęp do danych** z systemu gabinetowego (tylko zanonimizowanych lub zagregowanych): liczba wizyt, odwołania i nieobecności, obłożenie foteli, liczba nowych pacjentów, plany leczenia wystawione i przyjęte.

**Efekt fazy:** karta projektu na jedną stronę (cel, zakres, zespół, harmonogram, wskaźniki sukcesu).

### Faza 1: Inwentaryzacja procesów (tydzień 1–2)

7. **Spisz wszystkie procesy.** Skorzystaj z katalogu w §4 i dopasuj go do Dentalux podczas warsztatu burzy mózgów (1,5 godz. z zespołem roboczym).
8. **Narysuj mapę ogólną** (poziom 0) na jednej stronie: procesy podstawowe na środku, zarządcze u góry, wspierające na dole.
9. **Przygotuj SIPOC dla każdego procesu** (15–20 minut na proces, w arkuszu).
10. **Ustal priorytety** w macierzy: *wpływ na pacjenta i przychód* × *ryzyko (kliniczne, prawne)* × *poziom „bólu” zespołu*. Wybierz 5–7 procesów do szczegółowego mapowania (proponowana kolejność w §5).
11. **Przypisz każdemu procesowi właściciela** (process owner), jedną konkretną osobę, a nie dział.

### Faza 2: Mapa „jak jest” (tydzień 2–6)

Dla każdego priorytetowego procesu wykonaj pięć kroków:

12. **Obserwacja** (gemba, czyli praca na miejscu): 2–4 godz. w rejestracji, na zapleczu, w sterylizacji i przy przepływie pacjentów. **Poranek, szczyt popołudniowy i weekend na Racławickiej wyglądają zupełnie inaczej.** Notuj na papierze każdy krok, czas, przekazanie, zakłócenie i obejście.
13. **Wywiady indywidualne** (20–30 min) z każdą rolą. Kluczowe pytania:
    - „Opowiedz mi o ostatnim razie, kiedy…” (konkret, a nie „zazwyczaj”)
    - „Co najczęściej idzie nie tak?”
    - „Na co czekasz? Kto czeka na ciebie?”
    - „Co robisz inaczej niż jest w procedurze? Dlaczego?”
    - „Gdybyś mógł zmienić jedną rzecz…”
    - „Gdzie zapisujesz rzeczy, których nie ma w systemie?”
14. **Warsztat mapowania** (90–120 min, szary papier i karteczki) z przedstawicielami **wszystkich ról** biorących udział w procesie. Najpierw ścieżka typowa, potem **wyjątki**: pacjent się spóźnia, odwołuje, ma alergię, przychodzi z bólem, nie ma pieniędzy, praca z pracowni jest źle wykonana, nie działa CBCT, choruje lekarz.
15. **Pomiar:** czasy kroków, czasy oczekiwania, wolumeny, odsetek błędów. Wystarczy 1–2 tygodnie próbek na papierowym formularzu.
16. **Weryfikacja:** wystaw mapę na tablicy na tydzień. Pokaż ją osobom, które nie brały udziału w warsztacie. Przejdź proces „po mapie” z prawdziwym pacjentem, oczywiście bez zapisywania jego danych.

**Na mapie „jak jest” oznaczaj:**
- 🔴 straty (8 rodzajów strat w metodzie lean: oczekiwanie, zbędny ruch, zbędny transport, poprawki, nadprodukcja dokumentów, zapasy, nadmierne przetwarzanie, niewykorzystany potencjał ludzi)
- 🟠 przekazania między rolami, systemami i klinikami
- 🟣 punkty obowiązkowe z mocy prawa (compliance gates), których nie wolno pominąć (patrz §7)
- 🔵 systemy IT i dokumenty
- ⚠️ ryzyka dla bezpieczeństwa pacjenta

### Faza 3: Analiza (tydzień 6–7)

17. **Zestaw problemy w tabeli:** problem → gdzie na mapie → przyczyna źródłowa (5 × Dlaczego) → wpływ → trudność naprawy.
18. **Oddziel szybkie usprawnienia** (do wdrożenia w tydzień, bez kosztów) od **zmian strukturalnych** (system IT, nowe stanowisko, reorganizacja).
19. **Porównaj obie kliniki:** gdzie robią to samo inaczej i która wersja jest lepsza.

### Faza 4: Mapa „jak ma być” (tydzień 7–9)

20. **Zaprojektuj docelową wersję** 2–3 najważniejszych procesów z zespołem. Zasada: *najpierw uprość, potem ustandaryzuj, na końcu zautomatyzuj*.
21. **Przygotuj RACI dla nowych procesów.**
22. **Zdefiniuj wskaźniki dla każdego procesu** (patrz §6).
23. **Przeprowadź pilotaż** (cykl PDSA: zaplanuj, wykonaj, sprawdź, działaj) w jednej klinice przez 2–4 tygodnie, potem zmierz efekt, popraw i przenieś rozwiązanie do drugiej kliniki.

### Faza 5: Utrzymanie (od tygodnia 10, stale)

24. **Standardy pracy:** krótkie instrukcje na jedną stronę, najlepiej z obrazkami, przy stanowisku, a nie w segregatorze w szafie.
25. **Przegląd map co 6–12 miesięcy** albo przy każdej zmianie (nowy system, nowa usługa, nowy lekarz, nowe przepisy).
26. **Rejestr procesów jako żywy dokument:** właściciel, wersja, data przeglądu.
27. **Włącz mapy procesów do wdrażania nowych pracowników.** To często największa korzyść z całego projektu.

---

## 4. Typowe procesy w placówce stomatologicznej (katalog dla Dentalux)

### 4.1 Procesy podstawowe (ścieżka pacjenta)

| # | Proces | Kluczowe kroki | Specyfika Dentalux |
|---|---|---|---|
| P1 | **Pozyskanie pacjenta** | marketing, strona www, ZnanyLekarz, polecenia, opinie | Opinie z ZnanyLekarz to atut. Sprawdź, skąd przychodzą nowi pacjenci i czy ktoś to śledzi. |
| P2 | **Pierwszy kontakt i rejestracja** | telefon, www lub e-mail → dobór lekarza i rodzaju wizyty → termin → potwierdzenie (SMS lub e-mail) → przypomnienie | 4 kanały i 2 kliniki. Sprawdź, kto dobiera specjalistę, czy są skrypty rozmów, ile połączeń jest nieodebranych i jak szybko ktoś odpowiada na e-mail. |
| P3 | **Przyjęcie pacjenta** | powitanie → dane → ankieta medyczna (wywiad) → RODO → zgody → oczekiwanie | Czy ankieta jest papierowa, czy na tablecie? Czy jest wypełniana przed wizytą? |
| P4 | **Diagnostyka i konsultacja** | badanie → RTG, pantomogram, CBCT → skan lub zdjęcia → DSD | CBCT jako wspólny zasób. Opisy badań. Przepływ zdjęć między klinikami. |
| P5 | **Plan leczenia i jego akceptacja** | przygotowanie planu → wycena → prezentacja (lekarz lub koordynator) → decyzja → zaliczka lub raty → zaplanowanie serii wizyt | **Najważniejszy proces biznesowy.** Kto przedstawia plan? Czy ktoś kontaktuje się z pacjentem, który nie podjął decyzji? Czy plan jest zapisywany w systemie? |
| P6 | **Leczenie (wizyty zabiegowe)** | przygotowanie gabinetu → zabieg → dokumentacja → zalecenia → kolejna wizyta | Endodoncja, implanty, ortodoncja, protetyka i pedodoncja to osobne „podrodziny” procesu. |
| P6a | **Zabiegi w znieczuleniu ogólnym** | kwalifikacja, badania → anestezjolog → zgody → zabieg → wybudzenie → wypis | Wysokie ryzyko, więc potrzebna jest dokładna mapa. |
| P6b | **Proces protetyczny z pracownią** | wycisk lub skan → zlecenie → pracownia → dostawa → przymiarka → poprawki → oddanie pracy | Kluczowe przekazanie zewnętrzne. |
| P6c | **Leczenie ortodontyczne i Invisalign** | diagnostyka → ClinCheck → zamówienie → wizyty kontrolne co 6–10 tygodni → retencja | Leczenie trwa latami. Pilnowanie terminów wizyt kontrolnych. |
| P7 | **Rozliczenie i płatność** | rozliczenie wizyty → paragon lub faktura → raty, rabaty → rozliczenia wieloetapowe | Uzgodnienie wyceny w planie z tym, co pacjent faktycznie płaci. |
| P8 | **Zakończenie wizyty i kolejny termin** | zalecenia → umówienie kolejnej wizyty **przed wyjściem** pacjenta | Pacjent, który wychodzi bez kolejnego terminu, to najczęstszy „wyciek” pacjentów. |
| P9 | **Wizyty kontrolne i higienizacja (recall)** | przypomnienie co 6 lub 12 miesięcy → umówienie → higienizacja → przegląd | Źródło stałego przychodu i nowych planów leczenia. |
| P10 | **Opieka po zabiegu, gwarancje, reklamacje** | kontakt po zabiegu → komplikacje → reklamacja → naprawa gwarancyjna | Kto dzwoni po ekstrakcji lub wszczepieniu implantu? Jakie są zasady gwarancji? |
| P11 | **Nagłe przypadki (ból)** | telefon → wolne okienka w grafiku → wizyta w trybie pilnym | Weekendy są tylko na Racławickiej. Kto decyduje o przyjęciu pacjenta w trybie pilnym? |

### 4.2 Procesy wspierające

| # | Proces | Uwagi |
|---|---|---|
| W1 | **Sterylizacja i przygotowanie narzędzi** | Obieg: brudne → mycie → dezynfekcja → pakowanie → autoklaw → kontrola wskaźników → magazyn sterylny → gabinet. Śledzenie pakietów (kto, kiedy, który cykl). Krytyczne kontrolnie. |
| W2 | **Zaopatrzenie i magazyn** | Materiały, implanty (numery serii i możliwość śledzenia partii), leki, terminy ważności, minimalne stany, zamówienia. |
| W3 | **Odpady medyczne** | Segregacja, kody odpadów, magazynowanie, odbiór, ewidencja w systemie BDO. |
| W4 | **Sprzęt: przeglądy i awarie** | Fotele (unity), autoklawy, RTG i CBCT (testy), mikroskopy, laser, kompresory, ssaki. Paszporty techniczne. |
| W5 | **Ochrona radiologiczna** | Dozymetria, testy podstawowe i specjalistyczne, zezwolenia i zgłoszenia do PAA, procedury wzorcowe, rejestr dawek, szkolenia. |
| W6 | **Dokumentacja medyczna** | Prowadzenie, udostępnianie (np. pacjentom i sądom), archiwizacja, EDM, e-recepta, zdarzenia medyczne w P1. |
| W7 | **IT i system gabinetowy** | Konta, uprawnienia, kopie zapasowe, awarie, integracje (ZnanyLekarz, SMS, płatności). |
| W8 | **Współpraca z pracowniami i dostawcami zewnętrznymi** | Umowy, terminy, reklamacje, ocena dostawców. |
| W9 | **Utrzymanie czystości i infrastruktury** | Sprzątanie stref (czysta i brudna), plan higieny. |

### 4.3 Procesy zarządcze

| # | Proces | Uwagi |
|---|---|---|
| Z1 | **Grafik lekarzy i foteli** | Najważniejszy proces zarządczy, bo decyduje o przychodzie. Kto układa grafik, z jakim wyprzedzeniem, co się dzieje przy nieobecności lekarza. |
| Z2 | **Rekrutacja, wdrożenie, szkolenia, kompetencje** | Szczególnie asysty i rejestracja, gdzie rotacja jest wysoka. Szkolenia BHP, RODO, radiologiczne, pierwsza pomoc (wstrząs anafilaktyczny). |
| Z3 | **Współpraca z lekarzami** | Rozliczenia procentowe lub B2B, standardy, wprowadzanie nowego lekarza. |
| Z4 | **Jakość i zdarzenia niepożądane** | Zgłaszanie, analiza, działania korygujące. Skargi pacjentów. |
| Z5 | **Zgodność z przepisami (compliance)** | RODO (w tym inspektor ochrony danych), Sanepid, PAA, NFZ nie dotyczy, rejestr podmiotów wykonujących działalność leczniczą, ubezpieczenie OC. |
| Z6 | **Finanse i kontroling** | Cennik, marże na usługach, koszty materiałów, rozliczenia z lekarzami, raporty. |
| Z7 | **Marketing i opinie** | Strona www, ZnanyLekarz, odpowiedzi na opinie, rozwój ofert. |
| Z8 | **Strategia i rozwój** | Nowe usługi, inwestycje w sprzęt, projekty (także ten). |

---

## 5. Kolejność prac: czym zająć się po kolei

| Kolejność | Proces | Dlaczego teraz |
|---|---|---|
| **1** | Mapa ogólna (poziom 0) i SIPOC dla wszystkich procesów | Daje pełny obraz i ustala wspólny język. Zajmuje mało czasu, a daje dużo. |
| **2** | **P2 Rejestracja** oraz **P8 Kolejny termin i recall** | Tu łatwo widać problemy, szybko przychodzą usprawnienia, a zyskuje każdy pacjent. Zwykle to też miejsce z największym potencjałem automatyzacji i AI (voicebot, SMS, przypomnienia). |
| **3** | **P4 → P5 Diagnostyka → plan leczenia → akceptacja** | Największy wpływ na przychód. Warto tu zrobić VSM (czas od pierwszego kontaktu do rozpoczęcia leczenia). |
| **4** | **W1 Sterylizacja** i **W5 Ochrona radiologiczna** | Bezpieczeństwo pacjenta i ryzyko kontroli. Są opisane przepisami, więc mapuje się je szybko. |
| **5** | **P6b Proces protetyczny z pracownią** i **P6a Znieczulenie ogólne** | Złożone przekazania i wysokie ryzyko. |
| **6** | **Z1 Grafik i obłożenie foteli** | Wymaga danych z punktów 2–3. |
| **7** | Pozostałe: W2, W3, W6, P10, Z2–Z8 | Według priorytetów z fazy 1. |

---

## 6. Połączenia między procesami: co wpływa na co

### 6.1 Schemat głównych zależności

```
          ┌───────────── Z1 Grafik lekarzy i foteli ─────────────┐
          │ (ogranicza dostępność terminów dla wszystkich)       │
          ▼                                                      │
P1 Pozyskanie → P2 Rejestracja → P3 Przyjęcie → P4 Diagnostyka → P5 Plan leczenia
                     ▲                              │ ▲              │ (akceptacja?)
                     │                        W5 RTG/CBCT            ├── NIE → kontakt z pacjentem (często go brak!)
                     │                              │                ▼
                     │                              └─────── P6 Leczenie ←── W1 Sterylizacja
                     │                                          │  │     ←── W2 Magazyn/implanty
                     │                                          │  └──→ P6b Pracownia → (termin wraca do P2)
                     │                                          ▼
                     │                                    P7 Płatność ──→ Z6 Finanse
                     │                                          ▼
                     └────────────── P9 Recall ◀──────── P8 Kolejny termin
                                         │
                                         └──→ nowy P4/P5 (ok. 30–50% planów leczenia w klinikach
                                              prywatnych zaczyna się od przeglądu: szacunek, do sprawdzenia)

W6 Dokumentacja i Z5 Compliance przechodzą przez wszystko. P10 Reklamacje wracają do P6 i Z4.
```

### 6.2 Kluczowe zależności i przekazania

| Z procesu | Do procesu | Co się przekazuje | Typowa awaria | Skutek |
|---|---|---|---|---|
| P2 Rejestracja | P6 Leczenie | Rodzaj wizyty, czas, lekarz, informacja o potrzebie CBCT lub sedacji | Źle dobrany rodzaj lub długość wizyty | Opóźnienia przez cały dzień, lekarz bez przygotowania, pacjent umówiony „na nowo” |
| P3 Przyjęcie | P6 Leczenie | Wywiad medyczny (leki przeciwkrzepliwe, alergie, ciąża, bisfosfoniany) | Stary lub niepełny wywiad | **Ryzyko kliniczne** (krwawienie, reakcja alergiczna) |
| P4 Diagnostyka | P5 Plan leczenia | Zdjęcia, CBCT, skany, opisy | Badania „gdzieś są”, brak opisu, druga klinika nie ma dostępu | Powtórne badanie (dodatkowa dawka promieniowania i koszt), opóźnienie planu |
| P5 Plan leczenia | P7 Płatność | Wycena, rabat, raty | Plan zmienia się w trakcie leczenia, a wycena nie | Spór z pacjentem, strata finansowa |
| P5 Plan leczenia | P2 Rejestracja | Seria wizyt w odpowiednich odstępach | Wizyty umawiane pojedynczo | Wydłużone leczenie, pacjent „ginie” w środku |
| P6 Leczenie | P6b Pracownia | Zlecenie, kolor, skan, termin | Niekompletne zlecenie, brak ustalonego terminu | Przymiarka bez pracy z pracowni, wizyta zmarnowana |
| P6b Pracownia | P2 Rejestracja | Data dostawy | Rejestracja nie wie, że praca przyszła lub nie przyszła | Pacjent przychodzi na darmo |
| W1 Sterylizacja | P6 Leczenie | Komplety narzędzi | Za mało kompletów w szczycie (np. do chirurgii i implantów) | Wstrzymane zabiegi, pokusa skracania cyklu (ryzyko!) |
| W2 Magazyn | P6 Leczenie | Implanty, materiały | Brak konkretnego rozmiaru implantu | Przesunięty zabieg |
| W5 Ochrona radiologiczna | P4 Diagnostyka | Sprawny i przetestowany aparat | Awaria lub zaległy test | CBCT wyłączone, pacjenci odsyłani |
| P8 Kolejny termin | P9 Recall | Data kolejnej kontroli | Brak terminu lub przypomnienia | Utrata pacjenta. Najdroższy „cichy” błąd. |
| Z1 Grafik | wszystkie podstawowe | Dostępność | Nieobecność lekarza, dziury w grafiku | Przekładanie wizyt, niezadowolenie pacjentów |
| P10 Reklamacje | Z4 Jakość | Informacja o problemie | Reklamacje obsługiwane nieformalnie | Brak nauki na błędach, ryzyko prawne |
| P6 (klinika A) | P6 (klinika B) | Pacjent przechodzi między klinikami (np. w weekend) | Brak dokumentacji lub planu w drugiej klinice | Pacjent opowiada wszystko od nowa |

### 6.3 Zasady, które warto zapamiętać

- **Proces na końcu ścieżki cierpi przez błędy na jej początku.** Zła rejestracja psuje dzień lekarza. Przyczyny szukaj zawsze w górę strumienia.
- **Zasoby wspólne** (CBCT, sterylizacja, anestezjolog, komplety chirurgiczne) są ukrytymi wąskimi gardłami. Na mapie trzeba je pokazać osobno.
- **Pętle zwrotne** (recall, kontakt po nieprzyjętym planie leczenia, reklamacje) są w klinikach najczęściej **niezmapowane i niczyje**, a to właśnie one decydują o przychodzie w długim okresie.
- **Każde przekazanie to ryzyko utraty informacji.** Mniej przekazań oznacza mniej błędów. W jednym opisanym przypadku kliniki stomatologicznej połączenie rejestracji, wstępnego badania i RTG w jeden nieprzerwany krok skróciło czas oczekiwania z 18 do 1 minuty (źródło w bibliografii).

---

## 7. Punkty obowiązkowe z mocy prawa, które trzeba oznaczyć na mapie

W procesie „jak ma być” te kroki są **nienegocjowalne**. Nie wolno ich „zoptymalizować” przez usunięcie.

| Obszar | Co wymusza w procesie | Podstawa (do weryfikacji z prawnikiem lub doradcą) |
|---|---|---|
| **Dokumentacja medyczna** | Zakres wpisów, ich forma i terminy, udostępnianie dokumentacji, okres przechowywania (co do zasady 20 lat) | Ustawa o prawach pacjenta i Rzeczniku Praw Pacjenta. Rozporządzenie MZ w sprawie dokumentacji medycznej (Dz.U. 2024 poz. 798) |
| **Zgody pacjenta** | Świadoma zgoda na zabiegi o podwyższonym ryzyku w formie pisemnej, informacja o ryzyku i alternatywach | Ustawa o zawodach lekarza i lekarza dentysty (art. 32–34) |
| **RODO** | Obowiązek informacyjny, podstawy przetwarzania, upoważnienia, rejestr czynności, umowy powierzenia (np. z ZnanyLekarz, bramką SMS, pracownią), zasady nagrywania rozmów | RODO, ustawa o ochronie danych osobowych |
| **EDM i P1** | e-recepta, zdarzenia medyczne, dostęp do IKP | Ustawa o systemie informacji w ochronie zdrowia |
| **Sterylizacja i higiena** | Procedury zapobiegania zakażeniom, dokumentowanie cykli i wskaźników | Ustawa o zapobieganiu oraz zwalczaniu zakażeń i chorób zakaźnych (art. 11). Kontrole Sanepidu |
| **Odpady medyczne** | Segregacja według kodów, czas magazynowania, ewidencja | Ustawa o odpadach, rozporządzenie w sprawie odpadów medycznych, BDO |
| **Ochrona radiologiczna** | Zezwolenia i zgłoszenia, testy aparatów, dozymetria, procedury wzorcowe, uzasadnienie ekspozycji, szkolenia | Prawo atomowe i rozporządzenia wykonawcze. PAA i Sanepid |
| **Prawa pacjenta** | Informacja, dostęp do dokumentacji, skargi | Ustawa o prawach pacjenta |
| **Znieczulenie ogólne** | Wymogi dotyczące personelu i sprzętu, kwalifikacja, monitorowanie | Standardy organizacyjne w anestezjologii (rozporządzenie MZ) |
| **Podmiot leczniczy** | Wymogi dotyczące pomieszczeń, regulamin organizacyjny, OC | Ustawa o działalności leczniczej |

> Standardy akredytacyjne CMJ dotyczą głównie szpitali, POZ i ambulatoryjnej opieki specjalistycznej, więc dla prywatnej kliniki stomatologicznej nie są obowiązkowe. Mogą jednak posłużyć jako **gotowa lista kontrolna dobrych praktyk** (zgody, zdarzenia niepożądane, prawa pacjenta).

---

## 8. Na co zwrócić uwagę (i czego się nie spodziewasz)

### 8.1 Niespodzianki, które pojawiają się prawie zawsze

1. **Procedura na papierze różni się od praktyki.** Segregator z procedurami sanitarnymi mówi jedno, a asysta w piątek o 20:00 robi drugie. Nie oceniaj tego. Zapisz i zapytaj „dlaczego”, bo obejście często jest mądrzejsze od procedury.
2. **Ukryte systemy równoległe:** zeszyty, Excel „pani z rejestracji”, WhatsApp z pracownią, kartki na monitorze, prywatny telefon lekarza do pacjentów. **To dane pacjentów poza systemem, czyli ryzyko RODO.** Traktuj to jako diagnozę, a nie donos.
3. **Każdy lekarz ma „swój” proces.** Ten sam zabieg wygląda inaczej u dwóch implantologów: inne zestawy narzędzi, inne materiały, inny czas. Asysty muszą to wszystko pamiętać. To ogromne źródło błędów i obciążenia.
4. **„Bohaterowie” procesu.** Jedna osoba (np. długoletnia koordynatorka) „wie wszystko” i trzyma proces w głowie. Gdy idzie na urlop, proces się sypie. Zidentyfikuj takie osoby i potraktuj z szacunkiem, bo ich wiedza jest bezcenna. Mapa ma ją utrwalić, a nie odebrać tej osobie znaczenie.
5. **Kliniki różnią się bardziej, niż zarząd myśli.** Zwykle różnią się grafikiem, sposobem pracy z pracownią, zgodami i rolą rejestracji.
6. **Ludzie będą chcieli od razu naprawiać.** Na warsztacie mapy „jak jest” ktoś zawsze powie „a powinno być…”. Zapisuj to na zielonych karteczkach w „parkingu pomysłów”, ale nie mieszaj stanu obecnego z docelowym.
7. **Opór lekarzy.** Lekarze mają mało czasu, „to nie ich problem”, a przy umowie B2B w ogóle nie muszą uczestniczyć. Skróć ich udział do minimum (wywiad 20 min i walidacja), pokaż korzyść dla nich (mniej czekania, lepiej przygotowany pacjent, mniej telefonów) i pozyskaj jednego lekarza jako rzecznika projektu.
8. **Twoje stanowisko wpływa na to, co usłyszysz.** Jeśli jesteś kojarzony z zarządem, ludzie powiedzą ci „oficjalną” wersję. Pomaga obserwacja, rozmowy nieformalne i anonimowa skrzynka na uwagi.
9. **Efekt Hawthorne'a.** Gdy ludzie wiedzą, że są obserwowani, pracują „lepiej”. Obserwuj dłużej, aż się przyzwyczają, i w różnych dniach.
10. **Mapowanie odsłoni problemy, o których wolałbyś nie wiedzieć** (np. skracanie cykli sterylizacji, niepełne zgody, nieprzekazane pieniądze). Ustal ze sponsorem **z góry**, jak postępujecie w takich przypadkach: zasada „just culture”, czyli poprawiamy systemy, a nie szukamy winnych, **z wyjątkiem** działań celowo nieuczciwych.
11. **Problemy z danymi.** Dane z systemu gabinetowego będą niepełne albo różnie wprowadzane (np. odwołanie oznaczone jako nieobecność). Pierwsze wskaźniki będą niedokładne, więc traktuj je jako orientacyjne.
12. **To trwa dłużej, niż myślisz.** Pierwsza mapa szczegółowa zajmie 2–3 razy więcej czasu niż zakładasz. Kolejne pójdą szybciej.

### 8.2 Dobre praktyki rysowania

- **Czasowniki w trybie czynności:** „Weryfikuje dane pacjenta”, a nie „Weryfikacja”.
- **Jedna karteczka to jedna czynność, jedna rola.**
- **Każdy proces ma jasny początek (zdarzenie wyzwalające) i koniec (wynik).**
- **Poziomy szczegółowości:** 0 (mapa ogólna), 1 (proces), 2 (diagram z torami, tu jest 80% wartości), 3 (instrukcja stanowiskowa). Nie mieszaj poziomów na jednym diagramie.
- **Mapuj wyjątki,** nie tylko ścieżkę typową. Najczęstsze 3–5 wyjątków to zwykle źródło 80% problemów.
- **Zapisuj czasy i wolumeny na mapie** (np. „~40 telefonów dziennie, 25% nieodebranych”).
- **Wersjonuj mapy:** data, autor, status (szkic, zweryfikowana, zatwierdzona).
- **Pokazuj perspektywę pacjenta:** co pacjent widzi i ile czeka na każdym etapie.

### 8.3 Bezpieczeństwo danych podczas projektu

- **Nie fotografuj** ekranów, grafików z nazwiskami, kartotek ani poczekalni z pacjentami.
- W notatkach używaj **„Pacjent A”**, a nie nazwisk.
- Obecność obserwatora w gabinecie podczas zabiegu wymaga **zgody pacjenta** (prawo do intymności). Obserwuj raczej przepływ poza gabinetem, a w gabinecie tylko za zgodą.
- Zdjęcia karteczek przed wrzuceniem do narzędzi AI lub chmury sprawdź pod kątem danych osobowych.
- Poinformuj inspektora ochrony danych o projekcie.

---

## 9. Wskaźniki: co mierzyć w każdym procesie

Benchmarki pochodzą głównie z rynku USA. **Traktuj je jako orientacyjne**, a własną linię bazową ustal w fazie 2.

| Proces | Wskaźnik | Orientacyjny cel |
|---|---|---|
| P2 Rejestracja | % nieodebranych połączeń, czas odpowiedzi na e-mail lub formularz, czas do pierwszego wolnego terminu | Nieodebrane <5–10%, odpowiedź <2 godz. roboczych |
| P2/P8 | Nieobecności (no-show) i odwołania w ostatniej chwili | Nieobecności ok. 3–8%, najlepsi <2% |
| Z1 | Obłożenie foteli i czasu lekarzy | 75–90% |
| P5 | Akceptacja planów leczenia (liczbowo i wartościowo) | ≥60–70% |
| P5 | Czas od konsultacji do decyzji; % planów z kontaktem po wizycie | — |
| P8/P9 | % pacjentów wychodzących z kolejnym terminem; realizacja wizyt kontrolnych | ≥85% |
| P1 | Nowi pacjenci miesięcznie według źródła | — |
| P6b | % prac z pracowni na czas; % poprawek | >95% na czas |
| W1 | Wyniki kontroli wskaźników sterylizacji, braki kompletów narzędzi | 0 niezgodności |
| P10/Z4 | Liczba reklamacji i zdarzeń niepożądanych, czas zamknięcia sprawy | — |
| Całość | Ocena pacjentów (NPS, ZnanyLekarz), czas oczekiwania w poczekalni | Czekanie <10 min |

---

## 10. Czego nie ująłeś w pytaniu, a warto wiedzieć

1. **Mapa procesów to narzędzie, a nie cel.** Jeśli nie wiadomo, do czego posłuży (wybór systemu, automatyzacja, standaryzacja, wdrożenia), skończy w szufladzie. Dlatego faza 0 jest najważniejsza.
2. **Mapa to fundament pod AI i automatyzację.** Zanim cokolwiek zautomatyzujesz (voicebot w rejestracji, przypomnienia, transkrypcja wizyt, obsługa zgód), musisz znać proces. **Automatyzacja złego procesu tylko szybciej produkuje błędy.** Mapa „jak jest” to też specyfikacja wymagań dla dostawców.
3. **Właściciel procesu jest ważniejszy niż diagram.** Proces bez właściciela zawsze się rozpada. Każdy proces z listy musi mieć jedną osobę odpowiedzialną za jego działanie i wskaźniki.
4. **Zaangażuj pacjentów.** Krótka ankieta (5 pytań) lub 5–10 wywiadów z pacjentami, a nawet „tajemniczy klient” (zadzwoń i umów się sam, w obu klinikach i przez wszystkie kanały), pokazują rzeczy niewidoczne od środka.
5. **Mapuj też procesy „nudne”, ale kosztowne:** faktury i rozliczenia z lekarzami, zamówienia implantów i ich śledzenie, przeglądy sprzętu. Tam często uciekają pieniądze.
6. **Ryzyko jest integralną częścią mapy.** Przy procesach klinicznych dodaj prostą analizę ryzyka (FMEA): *co może pójść źle → jak poważne → jak częste → jak wykrywamy*. Szczególnie w znieczuleniu ogólnym, sterylizacji, RTG i przy weryfikacji leków pacjenta.
7. **Ciągłość działania:** co się dzieje, gdy nie działa system gabinetowy, internet, telefon, CBCT albo autoklaw? Zmapuj **tryby awaryjne**. W klinice pracującej 7 dni w tygodniu to realne scenariusze.
8. **Zarządzanie zmianą:** 70% projektów zmian upada przez ludzi, a nie przez metodę. Komunikuj szybkie efekty, doceniaj zespół i pokazuj, co zmieniło się dzięki ich uwagom.
9. **Nie optymalizuj wszystkiego.** Procesy, które działają i nie bolą, wystarczy spisać. Energię kieruj tam, gdzie są problemy.
10. **Dokumenty wynikowe projektu** (lista kontrolna):
    - [ ] Karta projektu
    - [ ] Rejestr procesów (arkusz) z właścicielami
    - [ ] Mapa ogólna (poziom 0)
    - [ ] SIPOC dla wszystkich procesów
    - [ ] Diagramy „jak jest” z torami dla 5–7 procesów priorytetowych
    - [ ] Mapa ścieżki pacjenta
    - [ ] Lista problemów z przyczynami i priorytetami
    - [ ] Diagramy „jak ma być” i RACI dla 2–3 procesów
    - [ ] Zestaw wskaźników z linią bazową
    - [ ] Plan wdrożenia i pilotażu
    - [ ] Instrukcje stanowiskowe (1 strona każda)

---

## 11. Harmonogram (wersja przy pracy części etatu)

| Tydzień | Działania | Rezultat |
|---|---|---|
| 0–1 | Cel, sponsor, zespół, komunikacja, zebranie dokumentów, dostęp do danych | Karta projektu |
| 1–2 | Burza mózgów o procesach, mapa ogólna, SIPOC, priorytety | Rejestr procesów, mapa poziomu 0 |
| 2–3 | Obserwacja i wywiady: rejestracja, recall | Notatki, pomiary |
| 3–4 | Warsztat: P2/P8/P9 „jak jest”, weryfikacja | Diagram z torami, ścieżka pacjenta |
| 4–5 | Diagnostyka → plan leczenia (VSM), sterylizacja, RTG | Diagramy i VSM |
| 5–6 | Pracownia protetyczna, znieczulenie ogólne, grafik | Diagramy |
| 6–7 | Analiza, porównanie klinik, lista problemów | Raport diagnostyczny dla zarządu |
| 7–9 | Projekt „jak ma być”, RACI, wskaźniki, pilotaż w jednej klinice | Procesy docelowe i plan pilotażu |
| 10+ | Pilotaż, pomiar, przeniesienie do drugiej kliniki, instrukcje, cykl przeglądów | Standard |

**Szacowany nakład pracy zespołu:** warsztaty 6–8 × 1,5–2 godz. (4–6 osób), wywiady 15–25 × 30 min, twoja praca 1–2 dni w tygodniu.

---

## 12. Pytania do zadania w pierwszym tygodniu

1. Jaki system gabinetowy działa w Dentalux? Czy jest wspólny dla obu klinik?
2. Czy Dentalux ma własną pracownię protetyczną, czy współpracuje z zewnętrzną (albo z kilkoma)?
3. Ile osób pracuje w rejestracji, asyście, higienie, sterylizacji i administracji w każdej klinice?
4. Jaki jest model współpracy z lekarzami (etat, B2B, rozliczenie procentowe)?
5. Kto dziś koordynuje plany leczenia kompleksowego? Czy jest koordynator pacjenta?
6. Czy istnieją spisane procedury (poza sanitarnymi)? Kiedy były aktualizowane?
7. Jak działa przepływ pacjenta i dokumentacji między klinikami (np. w weekend)?
8. Kto odpowiada za RODO (inspektor ochrony danych), za ochronę radiologiczną i za kontakty z Sanepidem?
9. Jakie są 3 największe „bóle” zarządu i zespołu w tej chwili?
10. Czy są plany wdrożenia nowego systemu lub AI? Wtedy mapa powinna być dopasowana do tego celu.

---

## Źródła

**Dentalux**
- https://dentalux.pl · https://dentalux.pl/kontakt/ · https://dentalux.pl/zespol/ · https://dentalux.pl/nasza-oferta/
- https://www.znanylekarz.pl/placowki/centrum-stomatologii-dentalux

**Metodyka**
- NHS Improvement: *Process mapping, analysis and redesign*: https://www.england.nhs.uk/improvement-hub/wp-content/uploads/sites/44/2017/11/ILG-1.2-Process-Mapping-Analysis-and-Redesign.pdf
- IHI: *Quality Improvement Essentials Toolkit*: https://www.ihi.org/library/tools/quality-improvement-essentials-toolkit
- Antonacci i in., przegląd systematyczny process mappingu w ochronie zdrowia: https://pmc.ncbi.nlm.nih.gov/articles/PMC8048073/
- VSM w klinice stomatologicznej, *Revisiting lean healthcare…*: https://pmc.ncbi.nlm.nih.gov/articles/PMC12443820/
- Brown paper mapping (Umbrex): https://umbrex.com/resources/frameworks/process-improvement-frameworks/brown-paper-process-mapping/

**Wskaźniki (rynek USA, do kalibracji)**
- https://www.dentrixascend.com/insights/blogs/dental-practice-kpis-office-managers/
- https://sunrisedentalsolutions.com/dental-practice-key-performance-indicators-which-metrics-actually-drive-performance/

**Prawo i regulacje (PL)**
- Rozporządzenie MZ w sprawie dokumentacji medycznej, tekst jednolity: https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20240000798
- NIL, procedury w praktyce stomatologicznej: https://nil.org.pl/dla-lekarzy/dla-stomatologow/moja-praktyka/2297-procedury-medyczne
- Procedury Sanepidu w gabinecie stomatologicznym: https://medeq.pl/blog/procedury-sanepidu-gabinet-stomatologiczny-2026
- Centrum Monitorowania Jakości: https://www.cmj.gov.pl/

> Przepisy prawne w §7 to przegląd orientacyjny, a nie porada prawna. Przed zaprojektowaniem procesów docelowych zweryfikuj je z prawnikiem, inspektorem ochrony danych i inspektorem ochrony radiologicznej.
