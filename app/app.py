from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "v1.0.0")
APP_ENV     = os.getenv("APP_ENV", "local")

@app.route("/")
def home():
    return jsonify({
        "message": "Hello DevOps!",
        "version": APP_VERSION,
        "env":     APP_ENV,
        "host":    socket.gethostname()
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/ready")
def ready():
    return jsonify({"status": "ready"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
