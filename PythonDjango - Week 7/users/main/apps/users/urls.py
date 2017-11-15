from django.conf.urls import url
from . import views           

urlpatterns = [
	url(r'^$', views.index),
	url(r'^users/new$', views.new),
	url(r'^users/(?P<user_id>\d+)$', views.update),
	url(r'^users/(?P<user_id>\d+)/edit$', views.edit),
	url(r'^users/(?P<user_id>\d+)/delete$', views.delete)
] 