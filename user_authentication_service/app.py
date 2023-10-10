#!/usr/bin/env python3
""" Route module for the API
"""
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def Bienvenue():
    """ returns a message when the route / is requested """
    return jsonify({"status": "OK"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
