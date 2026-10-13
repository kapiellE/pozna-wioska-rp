
from flask import Flask, send_from_directory, jsonify, request
from flask_socketio import SocketIO, emit, join_room, leave_room
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parent

app = Flask(__name__, static_folder=str(ROOT), static_url_path="/files")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "city-watch-dev")

socketio = SocketIO(app, cors_allowed_origins="*")
players = {}

@app.route("/")
def home():
    return send_from_directory(str(ROOT), "index.html")

@app.route("/health")
def health():
    return jsonify(status="ok", game="CITY WATCH", players=len(players))

@socketio.on("connect")
def on_connect():
    sid = request.sid
    players[sid] = {"id": sid, "name": "Gracz", "x": 0, "y": 0}
    join_room("global")
    emit("players_update", list(players.values()), to="global")
    emit("welcome", {"id": sid, "players": list(players.values())})

@socketio.on("set_name")
def set_name(data):
    if request.sid in players:
        name = str(data.get("name", "Gracz"))[:20]
        players[request.sid]["name"] = name
        emit("players_update", list(players.values()), to="global")

@socketio.on("move")
def move_player(data):
    player = players.get(request.sid)
    if not player:
        return

    try:
        player["x"] = max(-100000, min(100000, float(data.get("x", 0))))
        player["y"] = max(-100000, min(100000, float(data.get("y", 0))))
    except (ValueError, TypeError):
        return

    emit("player_moved", player, to="global", include_self=False)

@socketio.on("chat_message")
def chat_message(data):
    player = players.get(request.sid)
    if not player:
        return

    message = str(data.get("message", ""))[:300].strip()
    if message:
        emit("chat_message", {
            "name": player["name"],
            "message": message
        }, to="global")

@socketio.on("disconnect")
def on_disconnect():
    player = players.pop(request.sid, None)
    if player:
        leave_room("global")
        emit("players_update", list(players.values()), to="global")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))
    socketio.run(app, host="0.0.0.0", port=port)
