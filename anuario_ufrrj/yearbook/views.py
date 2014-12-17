# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.core import serializers
from django.views import generic


from yearbook.models import Unidade_Organizacional
from yearbook.models import Pessoa
from yearbook.models import Cargo
from yearbook.models import Funcao
from yearbook.models import Sala
from yearbook.models import Lotacao


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
	uorg = get_object_or_404(Unidade_Organizacional, pk=uorg_id)

	sub_uorgs = uorg.get_sons
	lotacoes = Lotacao.objects.filter(uorg=uorg)
	pessoas = []
	for lotacao in lotacoes:
		pessoa = lotacao.pessoa
		pessoas.append(pessoa)

	salas = Sala.objects.filter(uorg=uorg)

	funcoes = Lotacao.objects.filter(uorg=uorg).exclude(funcao__isnull=True)

	return render(request, 'yearbook/index.html', {
			'uorg' 		: uorg,
			'sub_uorgs'	: sub_uorgs,
			'pessoas'	: pessoas,
			'lotacoes'	: lotacoes,
			'salas'		: salas,
			'funcoes'	: funcoes,
		})

def todas_salas_uorg(uorg):
	
	uorg_sons = uorg.get_sons()
	salas_vetor = uorg.get_salas()
	salas_uorg = {uorg : salas_vetor}

	for son in uorg_sons:
		salas_uorg.update(todas_salas_uorg(son))

	return salas_uorg


def salas_uorg(request, uorg_id):
	uorg = Unidade_Organizacional.objects.get(pk=uorg_id)

	salas = todas_salas_uorg(uorg)
	return salas

def recuperar_salas_autocomplete(request, sala_nome):
	salas = list(Sala.objects.filter(identificador__istartswith=sala_nome)) #

	json_salas = serializers.serialize('json', salas)

	return HttpResponse(json_salas)

def recuperar_pessoas_autocomplete(request, pessoa_nome):
	pessoas = list(Pessoa.objects.filter(nome__startswith=pessoa_nome))
	json_pessoas = serializers.serialize('json', pessoas)
	return HttpResponse(json_pessoas)

def pessoas_uorg(request, uorg_id):
	return None

def login(request):
	template = loader.get_template('yearbook/login.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def salvar_pessoa(request, user_id):
	return None

def salvar_uorg(request, user_id):
	return None

def salvar_sala(request, user_id):
	return None

def salvar_lotacao(request, user_id):
	return None







	