import socket
from flask import Flask, jsonify, request

app = Flask(__name__)

class Information:
    hostname = socket.gethostname()

@app.route("/status")
def get_status():
    headers = str(request.headers)
    output = 'hostname: {hostname}\nHeaders\n=======\n{headers}\n\n'.format(
        hostname=Information.hostname, headers=headers)
    return output
