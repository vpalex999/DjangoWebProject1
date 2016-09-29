from django.shortcuts import render, HttpResponse, Http404
from page.models import *

def index(request, cat_id):
    cats= Category.objects.all().order_by("name")
    if cat_id == None:
        cat=Category.objects.first()
    else:
        try:
            cat=Category.objects.get(pk=cat_id)
        except Category.DoesNotExist:
            raise Http404

    goods = Good.objects.filter(category=cat).order_by("name")
    #s = "Категория: "+cat.name+"<br><br>"
    #for good in goods:
    #    s = s+"("+str(good.pk)+")"+good.name+"<br>"
    #return HttpResponse(s)
    return render(request, "index.html", {"category":cat, "cats":cats, "goods":goods })

def category(request, cat_id):
    try:
        cat = Category.objects.get(pk=cat_id)
        s="Категория товара: "+"("+str(cat.pk)+")"+cat.name+"| "+cat.description
    except Category.DoesNotExist:
        raise Http404 
    
    return HttpResponse(s)


def good(request, good_id):
    cats=Category.objects.all().order_by("name")
    try:
        good=Good.objects.get(pk=good_id)
    except Good.DoesNotExist:
        raise Http404
    #s=good.name+"<br><br>"+good.category.name+"<br><br>"+good.description
    #if not good.in_stock:
    #    s=s+"<br><br>"+"Нет в наличии!"
    #return HttpResponse(s)
    return render(request, "good.html", {"cats":cats, "good":good})
