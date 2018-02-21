from flask import Flask, render_template, Blueprint, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./smash.db'
db = SQLAlchemy(app)


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    desc = db.Column(db.String(500), unique=False, nullable=True)

    def __repr__(self):
        return '<%r>' % self.name


character_blueprint = Blueprint('character', __name__, template_folder='templates')


@app.route('/')
def index():
    allChars = Character.query.all()
    return render_template('index.html',list=allChars)


@app.route('/character/<character>')
def character(character):
    nameInput = Character.query.filter_by(name=character).first()
    desc = nameInput.desc
    allChars = Character.query.all()
    return render_template('character.html', name=character,description=desc, list=allChars)


@app.route('/characters/')
def characters():
    allChars = Character.query.all()

    return render_template('characters.html', list=allChars)

@app.route('/rest/description/update', methods=['POST'])
def updateDescription():
    if request.method=='POST':
        name = request.form['name']
        desc = request.form['desc']
        if desc:
            query = Character.query.filter_by(name=name).first()
            query.desc = desc
            db.session.commit()
            return query.desc
        else:
            return 'No description given'


if __name__ == '__main__':
    app.run()
