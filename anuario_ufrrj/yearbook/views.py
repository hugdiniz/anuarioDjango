# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, Http404
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

class Pessoa_json:
	id = 0
	nome = ""
	cargo = ""
	funcao = ""


def index(request):
	try:
		uorg = Unidade_Organizacional()
		parent_uorgs_list = uorg.recuperar_unidades_raiz()
		return uorg_info(request, parent_uorgs_list[0].pk)

	except Unidade_Organizacional.DoesNotExist:
		raise Http404

def pessoa_info(request, pessoa_id):

	pessoa = Pessoa.objects.get(pk=pessoa_id)
	lotacoes_object = Lotacao.objects.filter(pessoa=pessoa)
	lotacoes = []
	for lotacao in lotacoes_object:
		lotacoes.append(lotacao.nome)
		

	
	# pjson = Pessoa_json(id=pessoa.pk,nome=pes.nome,cargo=pessoa.cargo, funcao=lotacao.funcao.nome)

	dicionario_pessoa = {
						'id' 	: pessoa.pk,
						'nome' 	: pessoa.nome,
						'cargo' : pessoa.cargo.nome,
						'funcao': lotacoes
						}

	json_pessoa = json.dumps(dicionario_pessoa)
	return HttpResponse(json_pessoa)
	

def uorg_info(request, uorg_id):
	try:
		uorg = Unidade_Organizacional.objects.get(pk=uorg_id)

		sub_uorgs = uorg.get_sons
		lotacoes = Lotacao.objects.filter(uorg=uorg)
		pessoas = []
		for lotacao in lotacoes:
			pessoa = lotacao.pessoa
			pessoas.append(pessoa)

		salas = Sala.objects.filter(uorg=uorg)

		template = loader.get_template('angularJS/index.html')

		context = RequestContext(request, {
			'uorg' 		: uorg,
			'sub_uorgs'	: sub_uorgs,
			'pessoas'	: pessoas,
			'salas'		: salas,
 			})

		return HttpResponse(template.render(context))

	except Unidade_Organizacional.DoesNotExist:
		raise Http404

	

def detail_cargo(request, cargo_id):
	return HttpResponse("Voce esta procurando o Cargo %s" % cargo_id)


	