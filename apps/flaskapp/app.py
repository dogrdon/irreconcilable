import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from forms import AddTermForm

app = Flask(__name__)
app.config.from_envvar('FLASKAPP_SETTINGS', silent=True)
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
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

def format_path(term):
    return term.lower().replace(" ", "_")

def grab_uri(term):
    return format_path(term)

#VIEWS
@app.route('/')
def index():
    return 'start here'

@app.route('/terms')
def terms():
    terms = Term.query.all()
    return render_template('terms.html', terms=terms)

@app.route('/new', methods=('GET', 'POST'))
def newTerm():
    form = AddTermForm(csrf_enabled=True)
    return render_template('new_term.html', form=form)

@app.route('/add_term', methods=('GET', 'POST'))
def addTerm():
    '''url for taking in the final disposition for list of results and posts to db'''
    #uri_pre = "http://example.org/"
    if request.method == "POST":
        termtxt = form.term_text.data
        newTerm = Term(term_text=termtxt)
        termUri = uri_pre + grab_uri(termtxt)
        db.session.add(newTerm)
        db.session.flush()
        newUri = Uri(uri=termUri, term_id=newTerm.id)
        db.session.add(newUri)
        db.session.commit()
        return redirect(url_for('terms'))
    else:
        return render_template('new_term.html', form=form)

@app.route('/term/<int:term_id>')
def term_details(term_id):
    return 'Term %d' % term_id



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
