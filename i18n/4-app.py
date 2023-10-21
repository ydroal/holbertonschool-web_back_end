#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel


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


@babel.localeselector
def get_locale():
    """
    Get locale from request
    """
    query = request.args.get('locale')
    if query in app.config['LANGUAGES']:
        return query
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=["GET"], strict_slashes=False)
def index():
    """ GET /
    Return:
      - 4-index.html
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
