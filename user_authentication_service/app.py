#!/usr/bin/env python3
""" Route module for the API
"""
from flask import Flask, jsonify, request, abort, redirect
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


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """
    POST /sessions
    Expect form data:
      - email: user's email
      - password: user's password

    Return:
      - JSON {"email": "<user email>", "message": "logged in"}
      - or 401 if the login information is incorrect
    """
    user_email = request.form.get('email')
    user_password = request.form.get('password')

    if not user_email or not user_password:
        abort(401)

    if not AUTH.valid_login(user_email, user_password):
        abort(401)

    user_session_id = AUTH.create_session(user_email)

    resp = jsonify({"email": user_email, "message": "logged in"})
    resp.set_cookie("session_id", user_session_id)
    return resp


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """
    DELETE /sessions
    Expect form data:
      - session_id: user's session id

    Return:
      - redirect to root page '/'
    """
    user_session_id = request.cookies.get("session_id")

    if not user_session_id:
        abort(403)

    user = AUTH.get_user_from_session_id(user_session_id)
    if not user:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect("/")


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """
    GET /profile
    Check the user's profile
      - session_id: user's session id

    Return:
      - If the user corresponding to session id exist, 200
      - If the session ID is invalid or the user does not exist, 403
    """
    user_session_id = request.cookies.get("session_id")
    if not user_session_id:
        abort(403)

    user = AUTH.get_user_from_session_id(user_session_id)
    if not user:
        abort(403)

    return jsonify({"email": user.email})


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """
    POST /reset_password
    Expect form data:
      - email: user's email

    Return:
      - If the user corresponding to session id exis, 403
      - Otherwise, generate a token and respond with a 200 and the JSON payload
    """
    user_email = request.form.get('email')

    if not user_email:
        abort(403)

    try:
        user_reset_token = AUTH.get_reset_password_token(user_email)
    except ValueError:
        abort(403)

    return jsonify({"email": user_email, "reset_token": user_reset_token})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
