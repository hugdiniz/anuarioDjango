# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core import serializers
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from yearbook.models import Unidade_Organizacional
from yearbook.models import Pessoa
from yearbook.models import Cargo
from yearbook.models import Funcao
from yearbook.models import Sala
from yearbook.models import Lotacao


import json



# Create your views here.

@login_required(login_url='login')
def index(request):
	try:
		uorg = Unidade_Organizacional()
		parent_uorgs_list = uorg.recuperar_unidades_raiz()
		return uorg_info(request, parent_uorgs_list[0].pk)

	except (Unidade_Organizacional.DoesNotExist, IndexError):
		raise Http404

@login_required(login_url='login')
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
			'user'		: request.user,
		})

@login_required(login_url='login')
def lotacao_info(request):
	if request.method == 'GET':
		lotacao_id = request.GET['lotacao_id']
		if lotacao_id:
			lotacao = Lotacao.objects.get(pk=lotacao_id)
			# json_funcao = serializers.serialize('json', lotacao)
			lotacao_dict = {
				'id'			: lotacao.pk,
				'nome'			: lotacao.nome,
				'pessoa'		: lotacao.pessoa.nome,
				'uorg'			: lotacao.uorg.nome,
				'sala'			: lotacao.sala.identificador,
				'funcao'		: lotacao.funcao,
				'entrada'		: lotacao.entrada,
				'afastamento'	: lotacao.afastamento, 
			}

			json_lotacao = json.dumps(lotacao.__dict__)
			return HttpResponse(lotacao.to_JSON)

def pessoa_info(request):

	pessoa_id = request.GET['pessoa_id']

	if pessoa_id:
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

def recuperar_salas_autocomplete_get(request, sala_nome):
	salas = list(Sala.objects.filter(identificador__istartswith=sala_nome)) #

	json_salas = serializers.serialize('json', salas)

	return HttpResponse(json_salas)

def recuperar_salas_autocomplete(request):
	# salas = list(Sala.objects.filter(identificador__istartswith=sala_nome)) #

	# json_salas = serializers.serialize('json', salas)

	# return HttpResponse(json_salas)
	return None


def recuperar_pessoas_autocomplete(request, pessoa_nome):
	pessoas = list(Pessoa.objects.filter(nome__startswith=pessoa_nome))
	json_pessoas = serializers.serialize('json', pessoas)
	return HttpResponse(json_pessoas)

def pessoas_uorg(request, uorg_id):
	return None

@login_required(login_url='login')
def pessoas_list(request):
	pessoas = list(Pessoa.objects.filter())

	return render(request, 'yearbook/pessoas.html', {
		'pessoas'	: pessoas,
		})


def render_login_page(request):
	if 'next' in request.GET:
		return render(request, 'yearbook/login.html', {
			'success'	: True,
			'next'		: request.GET['next'],
			})
	else:
		return render(request, 'yearbook/login.html', {
			'success'	: True,
			})

def efetuar_login(request):
	if request.method == 'POST':
		username = request.POST["username"]
		password = request.POST["password"]

		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				if request.POST['next']:
					return HttpResponseRedirect(request.POST['next'])
				else:
					return index(request)
		else:
			return render(request, 'yearbook/login.html', {
				'username'	: username,
				'success'	: False,
			})		


	# template = loader.get_template('yearbook/login.html')
	# context = RequestContext(request, {,})
	# return HttpResponse(template.render(context))

def efetuar_logout(request):
	logout(request)
	return render_login_page(request)


def salvar_pessoa(request, user_id):
	return None

def salvar_uorg(request, user_id):
	return None

def salvar_sala(request, user_id):
	return None

def salvar_lotacao(request, user_id):
	return None







	