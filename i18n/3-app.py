#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, render_template
from flask_babel import Babel, gettext
from flask import request


class Config(object):
    """
    Define Config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


def get_locale():
    """
    Get locale from request
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app, locale_selector=get_locale)


@app.route('/', methods=["GET"], strict_slashes=False)
def index():
    """ GET /
    Return:
      - 3-index.html
    """
    return render_template('3-index.html')


# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000)
