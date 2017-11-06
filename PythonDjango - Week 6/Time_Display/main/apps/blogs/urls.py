from django.conf.urls import url
from . import views           

urlpatterns = [
	url(r'^$', views.index),
	url(r'^new$', views.new),
	url(r'^create$', views.create),
	url(r'^(?P<number>\d+)$', views.show),
	url(r'^(?P<number>\d+)/edit$', views.edit),
	url(r'^(?P<number>\d+)/delete$', views.destroy),

	# url(r'^2003/$', views.special_case_2003),
	# url(r'^(?P<number>\d+)$', views.show),
	# url(r'^(?P<word>\w+)$', views.show_word),
	# url(r'^(?P<year>[0-9]{4})/$', views.show_word),
	# url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$')
] 