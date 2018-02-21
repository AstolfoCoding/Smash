from flask import Flask, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./smash.db'
db = SQLAlchemy(app)


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    desc = db.Column(db.String(120), unique=False, nullable=True)

    def __repr__(self):
        return '<%r>' % self.name


<<<<<<< HEAD
@app.route('/characters')
def characters():
    return 'characters'
=======
character_blueprint = Blueprint('character', __name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')

>>>>>>> b70da3595d5f44c36045702c7153a8256e2f2ce2


@app.route('/characters/<character>')
def characters(character):
    return render_template('characters.html', value=character)


if __name__ == '__main__':
    print(Character.query.filter_by(name='Mario').first())
    app.run()
