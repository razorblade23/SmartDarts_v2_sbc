from src.app import app, socketio

if __name__ == "__main__":
    host = "0.0.0.0"
    port = 5000
    print(f"Running on {host}:{port}")
    socketio.run(app, host="0.0.0.0", port=5000)
