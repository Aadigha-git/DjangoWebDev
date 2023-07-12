from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.

def index(response):
    return HttpResponse("<h1>Hello World!</h1>")

def id(response, id):
    ls = ToDoList.objects.get(id=id)
    item = ls.item_set.get(id = 1)
    return HttpResponse("<h2>%s</h2><br><p>%s<br>%s</p>" % (ls.name, item.text, item.complete))

def name1(response, name):
    ls = ToDoList.objects.get(name = name)
    return HttpResponse("<h3>%s</h3>" % ls.name)