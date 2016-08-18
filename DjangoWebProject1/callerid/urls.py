from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from callerid.views import CallerIDView

from . import views

urlpatterns = [
    #url(r'^$', views.callerid, name = 'callerid'),
    url(r'^$', views.CallerIDView.as_view(), name='callerid'),
    ]