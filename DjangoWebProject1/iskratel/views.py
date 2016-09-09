from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from iskratel.models import bookmarks
from iskratel.models import bookmarksubmenu
# Create your views here.


class IskratelView(TemplateView):
    template_name = "iskratel/iskratel.html"  # определяем шаблон отображения

    # определяем для шаблона контекст данных:
    # переопределяем метод
    def get_context_data(self, **kwargs):
        context = super(IskratelView, self).get_context_data() # вызвать метод из класса родителя
        context["nametab"] = bookmarks.objects.all() # добавить контекст, который содержит выборку имен закладок TAB в таблице bookmarks
        context["nametabsubmenu"] = bookmarksubmenu.objects.all() # добавить контекст для подменю, который содержит соответствие закладок TAB и подменю в таблице bookmarks
        return context # возвращаем контекст


class CallerID(TemplateView):
    template_name ="iskratel/callerid.html"
  


class Utility(TemplateView):
    template_name ="iskratel/utility.html"


class ReadNode(TemplateView):
    template_name ="iskratel/readnode.html"

