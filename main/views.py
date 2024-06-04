from sre_parse import CATEGORIES
from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render
from django.template import context
from django.template.defaultfilters import first
from goods.models import Category
# Create your views here.
def index(request):
    

   context={
       'title':'Home-Главная ',
       'content':"Магазин мебели HOME",
   }

   return render (request, 'main/index.html',context)


def about (request):
    context={
       'title':'Home-О нас  ',
       'content':"О нас",
       'text_on_page': "Текст о том что магазин крутой."
    }

    return render (request, 'main/about.html',context)