import json
from flask import Flask, Response, jsonify, render_template
from flask_cors import CORS, cross_origin
from markupsafe import escape

from flaskr.db import engine, text

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/languages')
@cross_origin()
def getLanuages():
    languages = load_languages_from_db()    
    
    return jsonify({'languages': [{
            'uuid': lang.uuid,
            'name': lang.name,
            'code': lang.code,
            'country': lang.country
        } for lang in languages]})
        

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
        languages = res.mappings().all()
        return languages

app.run(debug = True)