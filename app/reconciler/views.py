from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Term, Uri

def index(request):
	current_terms = Term.objects.order_by('-add_date')
	template = loader.get_template('reconciler/index.html')
	context = RequestContext(request, {'current_terms':current_terms})
    
	return HttpResponse(template.render(context))