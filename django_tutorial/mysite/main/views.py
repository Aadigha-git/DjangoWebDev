from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.

def home(response):
    return render(response, 'main/home.html', {})

def idx(response, id):
    ls = ToDoList.objects.get(id=id)
    #item = ls.item_set.get(id = id)
    # return HttpResponse("<h2>%s</h2><br><p>%s<br>%s</p>" % (ls.name, item.text, item.complete))
    return render(response, 'main/base.html', {})