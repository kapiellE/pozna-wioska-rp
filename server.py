"""Minimalny serwer plików dla gry (Render i inne hostingi z Pythonem).

Działa na dwa sposoby:
  * Render domyślnie uruchamia:  gunicorn server:app   (obiekt `app` poniżej)
  * lokalnie / ręcznie:          python server.py
Serwuje pliki z folderu repozytorium; adres / otwiera index.html.
"""
import mimetypes
import os

BASE = os.path.dirname(os.path.abspath(__file__))
HIDDEN = {"server.py", "requirements.txt"}


def app(environ, start_response):
    if environ.get("REQUEST_METHOD", "GET") not in ("GET", "HEAD"):
        start_response("405 Method Not Allowed", [("Content-Type", "text/plain"), ("Allow", "GET, HEAD")])
        return [b"Method Not Allowed"]

    path = environ.get("PATH_INFO", "/") or "/"
    if path.endswith("/"):
        path += "index.html"
    parts = [p for p in path.split("/") if p]
    full = os.path.normpath(os.path.join(BASE, *parts))

    forbidden = (
        not full.startswith(BASE + os.sep)
        or any(p.startswith(".") for p in parts)   # np. .git
        or os.path.basename(full) in HIDDEN
    )
    if forbidden or not os.path.isfile(full):
        start_response("404 Not Found", [("Content-Type", "text/plain; charset=utf-8")])
        return ["Nie znaleziono strony.".encode("utf-8")]

    ctype = mimetypes.guess_type(full)[0] or "application/octet-stream"
    if ctype.startswith("text/") or ctype in ("application/javascript", "application/json"):
        ctype += "; charset=utf-8"
    with open(full, "rb") as f:
        data = f.read()
    start_response("200 OK", [
        ("Content-Type", ctype),
        ("Content-Length", str(len(data))),
        ("Cache-Control", "no-cache"),   # zawsze świeża wersja gry
    ])
    return [] if environ.get("REQUEST_METHOD") == "HEAD" else [data]


if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    port = int(os.environ.get("PORT", "10000"))
    print(f"Serwer gry działa na porcie {port}", flush=True)
    make_server("0.0.0.0", port, app).serve_forever()
