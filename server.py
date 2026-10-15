"""Minimalny serwer plików dla gry (Render / dowolny hosting z Pythonem).
Serwuje pliki z folderu repozytorium (index.html pod adresem /) na porcie z zmiennej PORT.
"""
import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class Handler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # zawsze pobieraj świeżą wersję gry (bez starej kopii w pamięci przeglądarki)
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))
    print(f"Serwer gry działa na porcie {port}", flush=True)
    ThreadingHTTPServer(("0.0.0.0", port), Handler).serve_forever()
