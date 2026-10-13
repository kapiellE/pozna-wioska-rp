
from flask import Flask, send_from_directory, jsonify
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parent
GAME_DIR = ROOT / "static"

app = Flask(__name__, static_folder=str(GAME_DIR), static_url_path="/static")

@app.route("/")
def home():
    return send_from_directory(str(GAME_DIR), "index.html")

@app.route("/health")
def health():
    return jsonify(status="ok", game="CITY WATCH")

@app.errorhandler(404)
def not_found(error):
    return jsonify(error="Nie znaleziono pliku. Sprawdź folder static."), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
