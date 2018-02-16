from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./smash.db'
db = SQLAlchemy(app)

class Character(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),unique=True,nullable=False)
    desc = db.Column(db.String(120),unique=False,nullable=True)

    def __repr__(self):
        return '<%r>' % self.name

@app.route('/characters')
def characters():
    return 'characters'

@app.route('/characters/<character>')
def character_name(character):
    return character
