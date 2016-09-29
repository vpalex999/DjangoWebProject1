from django.conf.urls import url
from page import views

urlpatterns = [
    #url(r'^$', views.index, name="index"),
    #url(r'^good/$', views.good, name = "good"),
    #url(r'^(?:\?id=(?P<id>\d+))?$', views.index, name="index"),
    url(r'^(?:(?P<cat_id>\d+)/)?$', views.index, name='index'),
    url(r'^good/(?P<good_id>\d+)/$', views.good, name='good'),
    url(r'^cat/(?P<cat_id>\d+)/$', views.category, name='category'),
]