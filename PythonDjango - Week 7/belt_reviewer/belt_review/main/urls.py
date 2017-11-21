from django.conf.urls import url, include

urlpatterns = [
	url(r'^', include('apps.login_reg.urls', namespace = "login")),
	url(r'^books/', include('apps.belt.urls', namespace = "review")),
]
