# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from yearbook.models import Unidade_Organizacional
from django.core import serializers
import json

# Classes
class Uorg_tree:
	nome = ""
	id  = 0
	filhos = []

# Create your views here.


def index(request):
	uorg = Unidade_Organizacional()
	parent_uorgs_list = uorg.recuperar_unidades_raiz()

	template = loader.get_template('angularJS/index.html')

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
	return render(request, 'angularJS/index.html')

def get_sons_json(request, uorg_id):
	uorg = Unidade_Organizacional(id=uorg_id)
	result =  serializers.serialize("json", uorg.get_sons())
	return HttpResponse(result)

def preenche_arvore(uorg):
	json = Uorg_tree
	json.nome = uorg.nome
	
	for filho in uorg.get_sons:
		json.filhos = preenche_arvore(filho)

	return json

def get_arvore_menu(request):
	uorg = Unidade_Organizacional.objects.get(id=1)
	uorg


