from django.conf.urls import url
from . import views           

urlpatterns = [
	url(r'^$', views.index),
	url(r'^amadon/buy$', views.buy),
	url(r'^back$', views.back)

	
	# url(r'^session_words/add_word$', views.add_word),
	# url(r'^session_words/clear$', views.clear),
] 