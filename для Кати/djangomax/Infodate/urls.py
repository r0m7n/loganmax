from django.conf.urls import url
from .import views

app_name = 'Infodate'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^Infodate', views.primer, name='primer'),
]
