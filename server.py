
from flask import Flask, send_from_directory, jsonify, request
from flask_socketio import SocketIO, emit
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parent

app = Flask(__name__, static_folder=str(ROOT), static_url_path="/files")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "city-watch-secret")

socketio = SocketIO(app, cors_allowed_origins="*")
players = {}

@app.route("/")
def home():
    return send_from_directory(str(ROOT), "index.html")

@app.route("/health")
def health():
    return jsonify(status="ok", game="CITY WATCH", players=len(players))

@socketio.on("connect")
def connected():
    sid = request.sid
    players[sid] = {
        "id": sid,
        "name": "Gracz",
        "x": 100,
        "y": 100
    }
    emit("players_update", list(players.values()), broadcast=True)

@socketio.on("set_name")
def set_name(data):
    if request.sid not in players:
        return
    name = str(data.get("name", "Gracz")).strip()[:20]
    players[request.sid]["name"] = name or "Gracz"
    emit("players_update", list(players.values()), broadcast=True)

@socketio.on("move")
def move_player(data):
    player = players.get(request.sid)
    if not player:
        return
    try:
        player["x"] = max(0, min(2000, float(data["x"])))
        player["y"] = max(0, min(2000, float(data["y"])))
    except (KeyError, TypeError, ValueError):
        return
    emit("player_moved", player, broadcast=True, include_self=False)

@socketio.on("chat_message")
def chat_message(data):
    player = players.get(request.sid)
    if not player:
        return
    message = str(data.get("message", "")).strip()[:250]
    if message:
        emit("chat_message", {
            "name": player["name"],
            "message": message
        }, broadcast=True)

@socketio.on("disconnect")
def disconnected():
    players.pop(request.sid, None)
    emit("players_update", list(players.values()), broadcast=True)

if __name__ == "__main__":
    socketio.run(
        app,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", "10000"))
    )
