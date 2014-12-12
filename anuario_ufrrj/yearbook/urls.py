# -*- coding: utf-8 -*-z
from django.conf.urls import patterns, url
from yearbook import views

urlpatterns = patterns('',
	# anuario/index
	url(r'^$', views.index, name='index'),
	
	#urls referentes a uorg
	url(r'^/(?P<uorg_id>\d+)/$', views.uorg_info, name='uorg_info'),

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