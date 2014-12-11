from django.conf.urls import patterns, url
from yearbook import views

urlpatterns = patterns('',
	# anuario/index
	url(r'^$', views.index, name='index'),
	url(r'^pessoa/(?P<pessoa_id>\d+)/detail/$', views.detail_pessoa, name='pessoa_detail'),
	url(r'^uorg/(?P<uorg_id>\d+)/detail/$', views.detail_uorg, name='uorg_detail'),
	url(r'^cargo/(?P<cargo_id>\d+)/detail/$', views.detail_cargo, name='cargo_detail'),
	url(r'^template/$', views.polymer, name='polymer'),

	###################
	# AJAX URLs
	###################

	url(r'^uorg/(?P<uorg_id>\d+)/sons/$', views.get_sons_json, name='uorg_sons'),
)