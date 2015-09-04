from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from .models import Term, Uri
from .forms import NewTermForm

def index(request):
	current_terms = Term.objects.order_by('-add_date')
	
	form = NewTermForm(request.POST or None)

	if form.is_valid():
		new_term = form.save(commit = False)
		new_term.save()
	
	context = {
		"form": form,
		"current_terms": current_terms
	}
    
	return render(request, 'reconciler/index.html', context)


def term_info(request, term_id):
	term = get_object_or_404(Term, pk=term_id)
	context = {
		'term':term,
	}
	return render(request, 'reconciler/detail.html', context)

	