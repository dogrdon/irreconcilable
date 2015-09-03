from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from .models import Term, Uri
from .forms import NewTermForm

def index(request):
	current_terms = Term.objects.order_by('-add_date')
	template = loader.get_template('reconciler/index.html')
	context = RequestContext(request, {'current_terms':current_terms})
    
	return HttpResponse(template.render(context))

def term_info(request, term_id):
	term = get_object_or_404(Term, pk=term_id)
	return render(request, 'reconciler/detail.html', {'term':term})


def term_recon(request):

	form = NewTermForm(request.POST or None)

	if form.is_valid():
		new_term = form.save(commit = False)
		new_term.save()
	context = {
		"form": form
	}

	#return HttpResponse(template.render(context))
	#return HttpResponseRedirect('/reconciler')
	return render(request, 'reconciler/', context)
	