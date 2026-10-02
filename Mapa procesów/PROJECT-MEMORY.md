# PROJECT-MEMORY: Mapa procesów Dentalux

**Lokalizacja:** `C:\Users\Marcin Kasiak\ClaudeFiles\01_Praca\01-projekty-w-trakcie\Mapa procesów\`
**Start:** 2026-09-25 · **Właściciel:** Marcin Kasiak · **Status:** faza 0 (przygotowanie)

## Cel

Przygotować mapę procesów Centrum Stomatologii Dentalux (Racławicka 131 i Puławska 257). Mapa ma posłużyć do standaryzacji obu klinik i stać się podstawą do wyboru oraz wdrożenia systemów IT, automatyzacji i AI.
Szczegółowy plan: `2026-09-25-mapa-procesow-dentalux-plan.html` (źródło: `raport/…plan.md`).

## Struktura folderu

| Ścieżka | Zawartość |
|---|---|
| `2026-09-25-mapa-procesow-dentalux-plan.html` | Raport z planem krok po kroku (styl drkasiak.pl). Otwórz w przeglądarce. |
| `raport/2026-09-25-mapa-procesow-dentalux-plan.md` | Źródło raportu (Markdown). Tutaj wprowadzaj zmiany. |
| `narzedzia/build_html.py` | Odbudowuje HTML z Markdown: `pip install markdown` → `python narzedzia/build_html.py` |
| `rejestr-procesow.csv` | Rejestr procesów (do Excela): ID, nazwa, typ, właściciel, priorytet, status mapy |
| `materialy/obserwacje/` | Notatki z obserwacji i wywiadów, zdjęcia map z karteczek (**bez danych pacjentów!**) |
| `materialy/mapy/` | Diagramy draw.io, osobno dla każdego procesu |

## Stan obecny

- [x] Raport z planem i metodyką (2026-09-25)
- [x] Wersja HTML w stylu drkasiak.pl
- [x] Szablon rejestru procesów (31 procesów z katalogu §4 raportu)
- [ ] Faza 0: cel ze sponsorem, karta projektu, zespół roboczy, komunikacja do personelu
- [ ] Odpowiedzi na 10 pytań z §12 raportu

## Następne kroki

1. Ustalić z zarządem cel mapy (standaryzacja, system IT, AI, akredytacja) i sponsora.
2. Odpowiedzieć na pytania z §12: system gabinetowy, własna czy zewnętrzna pracownia protetyczna, model współpracy z lekarzami, liczba osób w poszczególnych rolach.
3. Skompletować zespół roboczy i ogłosić projekt zespołowi („mapujemy procesy, a nie ludzi”).
4. Przeprowadzić warsztat burzy mózgów o procesach, przygotować mapę ogólną (poziom 0) i SIPOC. Uzupełnić `rejestr-procesow.csv`.
5. Zacząć obserwację od rejestracji (P2) oraz kolejnego terminu i recall (P8/P9).

## Znane problemy / techdebt

- Fakty o Dentalux pochodzą z publicznej strony www. Wymagają potwierdzenia wewnętrznego, zwłaszcza pracownia protetyczna, system IT, zatrudnienie i umowy B2B.
- Benchmarki wskaźników (§9) pochodzą z rynku USA. Trzeba ustalić własną linię bazową.
- Przegląd przepisów (§7) jest orientacyjny. Trzeba go zweryfikować z prawnikiem, inspektorem ochrony danych i inspektorem ochrony radiologicznej. Część podstaw prawnych podano z wiedzy modelu, bez sprawdzenia w źródłach.
- HTML pobiera czcionki z Google Fonts. Bez internetu wyświetla czcionki systemowe.

## Historia decyzji

- **2026-09-25:** Metodyka: najpierw mapa ogólna i SIPOC, potem szczegółowe diagramy z torami dla 5–7 procesów priorytetowych, a mapa docelowa i pilotaż w jednej klinice.
- **2026-09-25:** Narzędzia: papier i karteczki w terenie, draw.io jako repozytorium map, arkusz jako rejestr. BPMN tylko do automatyzacji.
- **2026-09-25:** Kolejność: rejestracja i recall → diagnostyka i plan leczenia → sterylizacja i RTG → pracownia protetyczna i znieczulenie ogólne → grafik.
- **2026-10-02:** Utworzono projekt w `01-projekty-w-trakcie\Mapa procesów`.
