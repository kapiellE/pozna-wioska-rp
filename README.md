# CITY WATCH — Miejskie RP 3D

Przeglądarkowa gra roleplay 3D (Three.js) w jednym pliku HTML.
Role: **Policja, Straż pożarna (OSP), PRM (ratownictwo medyczne), Pomoc drogowa, Cywil**.

## Sterowanie

| Klawisz | Akcja |
|---|---|
| W / S / A / D | przód / tył / lewo / prawo (pieszo i w aucie) |
| Prawy przycisk myszy (przytrzymaj) | kamera |
| E | wsiądź / wysiądź (w multiplayerze także jako pasażer cudzego auta, do 4 osób) |
| F | sygnały (policja, straż, PRM) |
| H | pomoc / zabranie poszkodowanego / legitymowanie / holowanie (zależnie od roli) |
| R | gaszenie (straż) |
| C / X / L | pachołek / zbierz pachołki / lizak |
| / | czat (ENTER wysyła) |
| G | jakość grafiki (niska / wysoka / ultra z odbiciami nieba) |
| T | pora dnia: auto / dzień / noc (tylko u Ciebie) |

## Grafika

Cykl dnia i nocy (1 godzina w grze = 1 minuta, ten sam zegar dla wszystkich graczy), dynamiczne cienie,
niebo z chmurami, słońcem, księżycem i gwiazdami, odbicia nieba na lakierze aut, tekstury asfaltu, trawy,
tynku i dachówek, lampy i okna zapalane nocą. Na słabszym komputerze wciśnij **G**, żeby obniżyć jakość.

## Multiplayer

Na ekranie startowym wpisz **nick**. Domyślnie wszyscy trafiają na ten sam **serwer główny** i widzą ten sam świat.
Możesz wpisać własny **kod pokoju** (np. `MIASTO1`) — wtedy grają razem tylko osoby z tym samym kodem.
Zaznacz „Gra solo”, jeśli nie chcesz multiplayera. Pierwsza osoba w pokoju zostaje hostem; jeśli host wyjdzie,
pokój łączy się ponownie i hostem zostaje ktoś inny. Host co 8 sekund wysyła aktualny stan świata, więc nikt nie
„odjeżdża” od reszty.

Synchronizowane są: pozycje graczy, ich animacje (chodzenie, kucanie, skok, trzymane przedmioty), pojazdy
(także pojazd na lawecie), role i stroje, sygnały świetlne, dźwięk syren (słychać je tym głośniej, im bliżej, i z
odpowiedniej strony), czat,
pachołki, wypadki (opatrzenie poszkodowanego, zabranie go karetką, przesłuchanie świadków, odholowanie wraków)
oraz pożary. Gracz, który dołączy do trwającej gry, dostaje aktualny stan świata.
Nie są synchronizowane: ruch NPC i pieniądze (każdy gracz ma własne).

Multiplayer działa przez WebRTC (biblioteka PeerJS) i publiczny serwer pośredniczący PeerJS, więc nie potrzebuje
własnego serwera. Przy bardzo restrykcyjnych sieciach (np. niektóre sieci firmowe/szkolne) połączenie może się nie udać.

## Publikacja na GitHub Pages

1. Utwórz nowe repozytorium (**New repository**), np. `city-watch`, ustaw je jako **Public**.
2. Wgraj pliki z tego folderu: `index.html`, `README.md` i `.nojekyll` (**Add file → Upload files**).
3. Wejdź w **Settings → Pages**. W sekcji *Build and deployment* wybierz **Deploy from a branch**,
   gałąź **main** i folder **/ (root)**, potem **Save**.
4. Po 1–2 minutach gra będzie pod adresem `https://TWOJ-LOGIN.github.io/city-watch/`.

Gra wczytuje Three.js i PeerJS z internetu (cdnjs i unpkg), więc do działania potrzebuje połączenia z siecią.
