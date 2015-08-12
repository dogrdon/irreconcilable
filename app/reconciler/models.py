from django.db import models

class Term(models.Model):
	term_text = models.CharField(max_length=220)
	add_date = models.DateTimeField('date added')


