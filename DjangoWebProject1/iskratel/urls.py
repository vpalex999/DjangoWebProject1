from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from iskratel.views import IskratelView
from iskratel.views import CallerID

from . import views

urlpatterns = [
    url(r'^$', views.IskratelView.as_view(), name='iskratel'),
    url(r'^callerid.html$',CallerID.as_view(), name='callerid'),
    ]