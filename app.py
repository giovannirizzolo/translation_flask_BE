from flask import Flask, jsonify, render_template, request
from markupsafe import escape
import json

from flaskr.db import engine, text

app = Flask(__name__)

@app.route('/languages')
def getLanuages():
    languages = load_languages_from_db()
    return jsonify({'data': languages})

@app.route('/')
def hello():
    return jsonify({'message': 'Hello gays'})

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'

@app.route('/hello')
@app.route('/hello/<string:name>')
def handleHello(name=None):
    return render_template('hello.html', name=name)




def load_languages_from_db():
    with engine.connect() as connection:
        res = connection.execute(text("SELECT * FROM languages"))
        languages = []
        for row_lang in res.all():
            print(row_lang)
            languages.append(json.dumps(row_lang))
        
        return languages

app.run(debug = True)