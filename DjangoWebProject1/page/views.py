from django.shortcuts import render, HttpResponse
from page.models import *

def index(request):
    cat_id=request.GET["id"]
    if cat_id == None:
        cat=Category.objects.first()
    else:
        cat=Category.objects.get(pk=cat_id)
    
    goods = Good.objects.filter(category=cat).order_by("name")
    s = "Категория: "+cat.name+"<br><br>"
    for good in goods:
        s = s+"("+str(good.pk)+")"+good.name+"<br>"
    return HttpResponse(s)

def good(request):
    return ""
