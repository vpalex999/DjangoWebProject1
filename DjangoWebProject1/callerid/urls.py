from django.conf.urls import url
from callerid.views import CallerIDView

from . import views

urlpatterns = [
    #url(r'^$', views.callerid, name = 'callerid'),
    url(r'^$', views.CallerIDView.as_view(), name='callerid'),
    ]