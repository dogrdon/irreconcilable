from flask.ext.wtf import Form
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from wtforms import fields
from wtforms.validators import Email, InputRequired, ValidationError

class AddTermForm(Form):
	term = fields.StringField(InputRequired())
