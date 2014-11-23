from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from yearbook.models import Unidade_Organizacional

# Create your views here.
def index(request):
	uorg = Unidade_Organizacional()
	parent_uorgs_list = uorg.recuperar_unidades_raiz()
	template = loader.get_template('yearbook/index.html')
	context = RequestContext(request, {
		'parent_uorgs_list' : parent_uorgs_list,
		})
	return HttpResponse(template.render(context))

def detail_pessoa(request, pessoa_id):
	return HttpResponse("Voce esta detalhando a pessoa %s" % pessoa_id)

def detail_uorg(request, uorg_id):
	try:
		uorg = Unidade_Organizacional.objects.get(pk=uorg_id)
	except Question.DoesNotExist:
		raise Http404

	return HttpResponse("Voce esta detalhando a Unidade %s" % uorg_id)

def detail_cargo(request, cargo_id):
	return HttpResponse("Voce esta procurando o Cargo %s" % cargo_id)

def polymer(request):
	return render(request, 'polymer/index.html')