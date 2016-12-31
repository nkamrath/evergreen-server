from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^info/(?P<lightIpAddress>([0-9]{1,3}\.){3}[0-9]{1,3})/$', views.light_info, name='light_info'),
	url(r'^commandpost/$', views.light_command, name='light_command'),
    url(r'^/$', views.index, name='index'),
]