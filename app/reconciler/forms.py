from django import forms

from .models import Term

class NewTermForm(forms.ModelForm):
	class Meta:
		model = Term
		fields = ['term_text']

