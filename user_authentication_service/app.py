#!/usr/bin/env python3
""" Route module for the API
"""
from flask import Flask, jsonify, request
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/')
def Bienvenue():
    """ returns a message when the route / is requested """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """ POST /users
    Expect form data:
      - email: email of the user
      - password: password of the user

    Return:
      - JSON with the registered email and a confirming message
      - or 400 if the email is already registered
    """
    user_email = request.form.get('email')
    user_password = request.form.get('password')

    if not user_email or not user_password:
        return None

    try:
        new_user = AUTH.register_user(user_email, user_password)
        return jsonify({"email": new_user.email, "message": "user created"})

    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
