
from flask import Flask, send_from_directory, jsonify
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parent

app = Flask(__name__, static_folder=str(ROOT), static_url_path="/files")

@app.route("/")
def home():
    return send_from_directory(str(ROOT), "index.html")

@app.route("/health")
def health():
    return jsonify(status="ok", game="CITY WATCH")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))
    app.run(host="0.0.0.0", port=port)
