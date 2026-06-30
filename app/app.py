from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>OpenShift + Tekton Lab</h1>

    <b>Versão:</b> 5.0<br>
    <b>Hostname:</b> {socket.gethostname()}
    """

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
