from threading import Thread
from flask import Flask

def keep_alive():
    app = Flask("")

    @app.route("/")
    def home():
        return "Server is running"

    def run():
        app.run(host="0.0.0.0", port=8080)

    Thread(target=run).start()
