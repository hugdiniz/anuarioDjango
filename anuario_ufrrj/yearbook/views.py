# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from yearbook.models import Unidade_Organizacional
from django.core import serializers
import json



# Create your views here.


def index(request):
	try:
		uorg = Unidade_Organizacional()
		parent_uorgs_list = uorg.recuperar_unidades_raiz()

		template = loader.get_template('angularJS/index.html')

		context = RequestContext(request, {
			'parent_uorgs_list' : parent_uorgs_list,
			})
		return HttpResponse(template.render(context))

	except Unidade_Organizacional.DoesNotExist:
		raise Http404

def pessoa_info(request, pessoa_id):
	try:
		pessoa = Pessoa.objects.get(pk=pessoa_id)

	except Exception, e:
		raise
	else:
		pass
	finally:
		pass
		return HttpResponse("Voce esta detalhando a pessoa %s" % pessoa_id)

def uorg_info(request, uorg_id):
	try:
		uorg = Unidade_Organizacional.objects.get(pk=uorg_id)
		sub_uorgs = uorg.get_sons
		servidores = 

	except Question.DoesNotExist:
		raise Http404

	return HttpResponse("Voce esta detalhando a Unidade %s" % uorg_id)

def detail_cargo(request, cargo_id):
	return HttpResponse("Voce esta procurando o Cargo %s" % cargo_id)


	