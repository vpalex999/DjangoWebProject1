from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from iskratel.views import IskratelView

from . import views

urlpatterns = [
    url(r'^$', views.IskratelView.as_view(), name='iskratel'),
    ]