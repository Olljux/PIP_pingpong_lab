from flask import Flask
import os

app = Flask(__name__)

PORT = os.getenv("PORT", "5000")
MESSAGE = os.getenv("MESSAGE", "pong")

@app.route("/ping")
def ping():
    return MESSAGE

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(PORT))