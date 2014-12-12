# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from yearbook.models import Unidade_Organizacional
from yearbook.models import Pessoa
from yearbook.models import Cargo
from yearbook.models import Funcao
from yearbook.models import Sala
from yearbook.models import Lotacao
from django.core import serializers
import json



# Create your views here.


def index(request):
	try:
		uorg = Unidade_Organizacional()
		parent_uorgs_list = uorg.recuperar_unidades_raiz()
		return uorg_info(request, parent_uorgs_list[0].pk)

	except Unidade_Organizacional.DoesNotExist:
		raise Http404

def pessoa_info(request, pessoa_id):
	try:
		pessoa = Pessoa.objects.get(pk=pessoa_id)
		lotacao = Lotacao.objects.get(pessoa_id)
		return HttpResponse("Voce esta detalhando a pessoa %s" % pessoa_id)
	except Exception, e:
		raise Http404
	

def uorg_info(request, uorg_id):
	try:
		uorg = Unidade_Organizacional.objects.get(pk=uorg_id)
		parent_uorg = uorg.parent

		sub_uorgs = uorg.get_sons
		lotacoes = Lotacao.objects.filter(uorg=uorg)
		pessoas = []
		for lotacao in lotacoes:
			pessoas.append(lotacao)

		template = loader.get_template('angularJS/index.html')

		context = RequestContext(request, {
			'uorg' 		: uorg,
			'sub_uorgs'	: sub_uorgs,
			'pessoas'	: pessoas,
			'parent_uorg' : parent_uorg,
 			})

		return HttpResponse(template.render(context))

	except Unidade_Organizacional.DoesNotExist:
		raise Http404

	

def detail_cargo(request, cargo_id):
	return HttpResponse("Voce esta procurando o Cargo %s" % cargo_id)


	