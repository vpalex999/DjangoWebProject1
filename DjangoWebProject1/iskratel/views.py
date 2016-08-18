from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
# Create your views here.


class IskratelView(TemplateView):
    template_name = "iskratel/iskratel.html"
# Create your views here.
