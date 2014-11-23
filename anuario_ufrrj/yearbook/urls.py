from django.conf.urls import patterns, url
from yearbook import views

urlpatterns = patterns('',
	# anuario/index
	url(r'^$', views.index, name='index'),
	url(r'^pessoa/(?P<pessoa_id>\d+)/detail/$', views.detail_pessoa, name='pessoa_detail'),
	url(r'^uorg/(?P<uorg_id>\d+)/detail/$', views.detail_uorg, name='uorg_detail'),
	url(r'^cargo/(?P<cargo_id>\d+)/detail/$', views.detail_cargo, name='cargo_detail'),
	url(r'^template/$', views.polymer, name='polymer'),
	# url(r'^pessoa/(?P<pessoa_id>\d+)/$', views.detail_pessoa, name='pessoa_detail'),
	# ex.: anuario/pessoa/1
	# url(r'^pessoa/(?P<pessoa_id>\s+)/detail/$', views.detail_pessoa, name='pessoa_detail'),
	# # ex.: anuario/uorg/1
	# url(r'^(?P<uorg_id>\s+)/uorg/$', views.detail_uorg, name='uorg'),
	# url(r'^uorg/(?P<uorg_id>\d+)/$', views.detail_uorg, name='uorg_detail'),
	# # ex.: anuario/cargo/1
	# url(r'^cargo/(?P<cargo_id>\s+)/detail/$', views.detail_cargo, name='cargo_detail'),
)