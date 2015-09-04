from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'(?P<term_id>[0-9]+)/$', views.term_info, name='term_info'),
    
]
