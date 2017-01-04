from django.conf.urls import url
from page import views
#from page.twviews import GoodListView, GoodDetailView
from page.twlistviews import GoodDetailView, GoodListView
from page.twlistviews import GoodCreate, GoodUpdate, GoodDelete

urlpatterns = [
    #url(r'^$', views.index, name="index"),
    #url(r'^good/$', views.good, name = "good"),
    #url(r'^(?:\?id=(?P<id>\d+))?$', views.index, name="index"),
    #url(r'^(?:(?P<cat_id>\d+)/)?$', views.index, name='index'),
    #url(r'^good/(?P<good_id>\d+)/$', views.good, name='good'),
    #url(r'^cat/(?P<cat_id>\d+)/$', views.category, name='category'),
    url(r'^(?:(?P<cat_id>\d+)/)?$', GoodListView.as_view(), name='index'),
    url(r'^good/(?P<good_id>\d+)/$', GoodDetailView.as_view(), name='good'),
    url(r'^(?P<cat_id>\d+)/add/$', GoodCreate.as_view(), name="good_add"),
    url(r'^good/(?P<good_id>\d+)/edit/$', GoodUpdate.as_view(), name="good_edit"),
    url(r'^(?P<cat_id>\d+)/delete/$', GoodDelete.as_view(), name="good_delete"),
]