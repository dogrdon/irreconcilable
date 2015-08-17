from django.db import models

class Term(models.Model):
    term_text = models.CharField(max_length=220)
    add_date = models.DateTimeField('date added')

    def __unicode__(self):
    	return self.term_text

class Uri(models.Model):
    term = models.ForeignKey(Term)
    uri = models.CharField(max_length=500)
    
    def __unicode__(self):
    	return self.uri