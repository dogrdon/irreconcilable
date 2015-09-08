from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config.from_object('settings')
app.config.from_envvar('settings', silent=True)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./tmp/check.db' #this should not be here in the long run
db = SQLAlchemy(app)

#MODELS
class Term(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    term_text = db.Column(db.String(255), unique=True)

    def __init__(self, term_text):
        self.term_text = term_text

    def __repr__(self):
        return '<Term %r>' % self.term_text

class Uri(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uri = db.Column(db.String(255))
    term_id = db.Column(db.Integer, db.ForeignKey('term.id'))
    term = db.relationship('Term', backref=db.backref('terms', lazy='dynamic'))

#HELPER FUNCTIONS
def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.row
    return rv

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

#VIEWS
@app.route('/')
def index():
    return 'start here'

@app.route('/terms')
def terms():
    db = get_db()
    cur = db.execute('select term_text from terms order by id desc')
    terms = cur.fetchall()
    return render_template('terms.html', terms=terms)

@app.route('/term/<int:term_id>')
def term_details(term_id):
    return 'Term %d' % term_id




if __name__ == '__main__':
    app.run(host='0.0.0.0')
