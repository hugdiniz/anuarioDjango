# -*- coding: utf-8 -*-z
from django.conf.urls import patterns, url
from yearbook import views

urlpatterns = patterns('',
	# anuario/index
	url(r'^$', views.login, name='login'),
	url(r'^principal/$', views.index, name='index'),
	
	#urls referentes a uorg
	url(r'^(?P<uorg_id>\d+)/$', views.uorg_info, name='uorg_info'),
	url(r'^uorg/save/(?P<user_id>\d+)$', views.salvar_uorg, name='uorg_save'),
	# url(r'^pessoas/(?P<uorg_id>\d+)/$', views.pessoas_uorg, name='pessoas_uorg'),

	# urls referentes a pessoa
	url(r'^pessoa/(?P<pessoa_id>\d+)/detail/$', views.pessoa_info, name='pessoa_info'),
	url(r'^pessoa/save/(?P<user_id>\d+)$', views.salvar_pessoa, name='pessoa_save'),
	url(r'^pessoa/search/(?P<pessoa_nome>\w+)/$', views.recuperar_pessoas_autocomplete, name='pessoas_autocomplete'),

	#urls referentes a salas
	url(r'^sala/save/(?P<user_id>\d+)$', views.salvar_sala, name='sala_save'),
	url(r'^sala/(?P<uorg_id>\d+)/$', views.salas_uorg, name='salas_uorg'),
	url(r'^sala/search/(?P<sala_nome>\w+)/$', views.recuperar_salas_autocomplete_get, name='salas_autocomplete_get'),
	url(r'^sala/search/$', views.recuperar_salas_autocomplete, name='salas_autocomplete'),


	# urls referentes a lotacao
	url(r'^lotacao/save/(?P<user_id>\d+)$', views.salvar_lotacao, name='lotacao_save'),
	url(r'^lotacao/search/(?P<user_id>\d+)$', views.salvar_lotacao, name='lotacao_search'),

	

	# url(r'^template/$', views.polymer, name='polymer'),

	###################
	# AJAX URLs
	###################

	# url(r'^uorg/(?P<uorg_id>\d+)/sons/$', views.get_sons_json, name='uorg_sons'),
)