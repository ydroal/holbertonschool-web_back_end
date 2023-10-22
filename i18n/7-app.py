#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz


class Config(object):
    """
    Define Config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Returns a user dictionary
    """
    query = request.args.get('login_as')
    if not query:
        return None

    user = users.get(int(query))
    if not user:
        return None
    else:
        return user


@app.before_request
def before_request():
    """
    Request Preprocessing
    """
    user_info = get_user()
    g.user = user_info


@babel.localeselector
def get_locale():
    """
    Get locale from request
    """
    query = request.args.get('locale')
    if query in app.config['LANGUAGES']:
        return query

    if g.user:
        locale = g.user['locale']
        if locale in app.config['LANGUAGES']:
            return g.user['locale']

    locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    if locale:
        return locale

    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """
    Get timezone
    """
    tz = request.args.get('timezone')
    if tz:
        try:
            # 指定された文字列に基づいてタイムゾーンオブジェクトを返す
            timezone = pytz.timezone(tz)
            return timezone.zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.user:
        tz = g.user['timezone']
        try:
            timezone = pytz.timezone(tz)
            return timezone.zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    else:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/', methods=["GET"], strict_slashes=False)
def index():
    """ GET /
    Return:
      - 6-index.html
    """
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
