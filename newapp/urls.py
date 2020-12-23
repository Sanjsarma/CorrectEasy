from django.conf.urls import url
from . import views

app_name='newapp'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^index/$', views.index, name='index'),
    url(r'^results/$', views.info, name='info'),#result url
    url(r'^history/$', views.getHistory, name='history'),#history url
]
