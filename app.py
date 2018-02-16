from flask import flask
app = Flask(__name__)

@app.route('/characters')
def characters():
    return 'characters'

@app.route('/characters/<character>')
def character_name(character):
    return character
