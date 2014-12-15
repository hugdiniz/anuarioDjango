# -*- coding: utf-8 -*-z
from django.conf.urls import patterns, url
from yearbook import views

urlpatterns = patterns('',
	# anuario/index
	url(r'^$', views.login, name='login'),
	url(r'^principal/ $', views.index, name='index'),
	
	#urls referentes a uorg
	url(r'^(?P<uorg_id>\d+)/$', views.uorg_info, name='uorg_info'),
	url(r'^salas/(?P<uorg_id>\d+)/$', views.salas_uorg, name='salas_uorg'),
	# url(r'^pessoas/(?P<uorg_id>\d+)/$', views.pessoas_uorg, name='pessoas_uorg'),

	# urls referentes a pessoa
	url(r'^pessoa/(?P<pessoa_id>\d+)/detail/$', views.pessoa_info, name='pessoa_info'),

	#urls
	# url(r'^cargo/(?P<cargo_id>\d+)/detail/$', views.detail_cargo, name='cargo_detail'),

	# url(r'^template/$', views.polymer, name='polymer'),

	###################
	# AJAX URLs
	###################

	# url(r'^uorg/(?P<uorg_id>\d+)/sons/$', views.get_sons_json, name='uorg_sons'),
)