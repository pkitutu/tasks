from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'api'
urlpatterns  = [
	url(r'^create/$', views.create, name='create'),
	url(r'^list/$', views.list, name='list'),
	url(r'^show/(?P<pk>[0-9]+)/$', views.show, name='show'),
	url(r'^update/(?P<pk>[0-9]+)/$', views.update, name='update'),
	url(r'^delete/(?P<pk>[0-9]+)/$', views.delete, name='delete'),
]