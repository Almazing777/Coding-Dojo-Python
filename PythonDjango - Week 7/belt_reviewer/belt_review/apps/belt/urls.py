from django.conf.urls import url
from . import views           

urlpatterns = [
 	url(r'^$', views.index, name ="index"),
	url(r'^add$', views.add, name ="add"),
	url(r'^create', views.create, name='create'),
	url(r'^(?P<book_id>\d+)$', views.show),
	url(r'^(?P<book_id>\d+)/create$', views.create_additional),
	url(r'^users/(?P<user_id>\d+)$', views.show_user),
	url(r'^reviews/(?P<review_id>\d+)/delete$', views.delete_review),
] 