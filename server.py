from flask import Flask, send_from_directory, jsonify
from pathlib import Path

app = Flask(__name__, static_folder="static")
ROOT = Path(__file__).resolve().parent
GAME_DIR = ROOT / "static"

@app.get("/")
def home():
    return send_from_directory(GAME_DIR, "index.html")

@app.get("/health")
def health():
    return jsonify(status="ok", game="CITY WATCH")

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", "10000"))
    app.run(host="0.0.0.0", port=port)
