"""
Flask web application with Hello World message and funny cat picture.

This application displays a "Hello World" message and the hostname of the server it's running on.
Additionally, it shows a funny cat picture from an internet URL.
"""

import socket

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    """
    Renders the home page with "Hello World" and the host name.
    """
    hostname = socket.gethostname()
    return render_template("index.html", hostname=hostname)


if __name__ == "__main__":
    # Runs the Flask application on port 5000 and makes it accessible from any host.
    app.run(host="0.0.0.0", port=5000)
