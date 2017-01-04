from django.shortcuts import Http404
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator, InvalidPage
from page.models import *

class GoodListView(TemplateView):
    template_name="index.html"
    def get_context_data(self,**kwargs):
        context=super(GoodListView, self).get_context_data(**kwargs)
        context["cats"]=Category.objects.all().order_by("name")
        if kwargs["cat_id"]==None:
            context["category"]=Category.objects.first()
        else:
            try:
                context["category"]=Category.objects.get(pk=kwargs["cat_id"])
            except Category.DoesNotExist:
                raise Http404
        context["goods"]=Good.objects.filter(category=context["category"]).order_by("name")
        return context

class GoodDetailView(TemplateView):
    template_name="good.html"
    
    def get_context_data(self, **kwargs):
        context=super(GoodDetailView,self).get_context_data(**kwargs)
        context["cats"]=Category.objects.all().order_by("name")
        try:
            context["good"]=Good.objects.get(pk=kwargs["good_id"])
        except Good.DoesNotExists:
            raise Http404
        return context