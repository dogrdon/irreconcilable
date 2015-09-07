from flask import Flask
app = Flask(__name__)


#ROUTES
@app.route('/')
def index():
    return 'start here'

@app.route('/terms')
def terms():
    return 'terms will be here'

@app.route('/term/<int:term_id>')
def term_details(term_id):
    return 'Term %d' % term_id

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
