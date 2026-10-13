# CITY WATCH — Miejskie RP 3D

Przeglądarkowa gra roleplay 3D (Three.js) w jednym pliku HTML.
Role: **Policja, Straż pożarna (OSP), PRM (ratownictwo medyczne), Pomoc drogowa, Cywil**.

## Sterowanie

| Klawisz | Akcja |
|---|---|
| W / S / A / D | przód / tył / lewo / prawo (pieszo i w aucie) |
| Prawy przycisk myszy (przytrzymaj) | kamera |
| E | wsiądź / wysiądź |
| F | sygnały (policja, straż, PRM) |
| H | pomoc / zabranie poszkodowanego / legitymowanie / holowanie (zależnie od roli) |
| R | gaszenie (straż) |
| C / X / L | pachołek / zbierz pachołki / lizak |
| / | czat (ENTER wysyła) |

## Multiplayer

Na ekranie startowym wpisz **nick** i **kod pokoju**. Wszyscy, którzy wpiszą ten sam kod, grają razem.
Puste pole kodu = gra solo. Pierwsza osoba w pokoju zostaje hostem, jeśli host wyjdzie, pokój łączy się ponownie
i hostem zostaje ktoś inny.

Synchronizowane są: pozycje graczy, pojazdy, role i stroje, sygnały świetlne oraz czat.
Nie są synchronizowane: ruch NPC, wypadki, pożary i pieniądze (każdy gracz ma własne).

Multiplayer działa przez WebRTC (biblioteka PeerJS) i publiczny serwer pośredniczący PeerJS, więc nie potrzebuje
własnego serwera. Przy bardzo restrykcyjnych sieciach (np. niektóre sieci firmowe/szkolne) połączenie może się nie udać.

## Publikacja na GitHub Pages

1. Utwórz nowe repozytorium (**New repository**), np. `city-watch`, ustaw je jako **Public**.
2. Wgraj pliki z tego folderu: `index.html`, `README.md` i `.nojekyll` (**Add file → Upload files**).
3. Wejdź w **Settings → Pages**. W sekcji *Build and deployment* wybierz **Deploy from a branch**,
   gałąź **main** i folder **/ (root)**, potem **Save**.
4. Po 1–2 minutach gra będzie pod adresem `https://TWOJ-LOGIN.github.io/city-watch/`.

Gra wczytuje Three.js i PeerJS z internetu (cdnjs i unpkg), więc do działania potrzebuje połączenia z siecią.
