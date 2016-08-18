from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
# Create your views here.


class CallerIDView(TemplateView):
    template_name = "callerid/callerid.html"


def callerid(request):
    return HttpResponse("Hello, world!")
