#!/usr/bin/env python3
""" Module of views that handles all routes for the Session authentication
"""
from os import getenv
from flask import jsonify, request
from api.v1.views import app_views
from models.user import User


@app_views.route('/auth_session/login/', methods=['POST'],
                 strict_slashes=False)
def login():
    """
    POST /auth_session/login/

    Authenticate the user by verifying email and password

    Return:
      - JSON representation of the authenticated user if successful
      - Error message in JSON format otherwise.
    """
    user_email = request.form.get('email')
    if not user_email:
        return jsonify({"error": "email missing"}), 400

    user_password = request.form.get('password')
    if not user_password:
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': user_email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    create_user = None
    for user in users:
        if user.is_valid_password(user_password):
            create_user = user
            break
        else:
            return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(create_user.id)

    SESSION_NAME = getenv("SESSION_NAME")

    res = jsonify(create_user.to_json())
    res.set_cookie(SESSION_NAME, session_id)

    return res
