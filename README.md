# CITY WATCH — Miejskie RP 3D

Pakiet do uruchomienia gry w przeglądarce na Renderze.

## Publikacja na Render

1. Rozpakuj ZIP.
2. Wgraj wszystkie pliki i folder `static` do nowego repozytorium GitHub.
3. Na Render wybierz **New + → Blueprint** i wskaż repozytorium z plikiem `render.yaml`.
   Alternatywnie wybierz **New + → Web Service**, a następnie:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn server:app`
4. Po wdrożeniu otwórz adres Rendera. Gra znajduje się na stronie głównej `/`.
   Endpoint `/health` służy do sprawdzenia, czy serwer działa.

## Test lokalny

`pip install -r requirements.txt`

`python server.py`

Następnie otwórz `http://127.0.0.1:10000`.

## Ważne

To jest wersja przeglądarkowa gry z przesłanego pliku HTML. Render udostępnia ją przez internet,
ale ten pakiet **nie dodaje jeszcze prawdziwego trybu wieloosobowego** — rozgrywka i czat z
oryginalnego pliku działają lokalnie w przeglądarce. Three.js i fonty są pobierane z CDN,
więc do ich załadowania potrzebne jest połączenie z internetem.
