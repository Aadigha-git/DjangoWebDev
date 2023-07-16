from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.

def home(response):
    return render(response, 'main/home.html', {})

def idx(response, id):
    ls = ToDoList.objects.get(id=id)
    #item = ls.item_set.get(id = id)
    if response.method == "POST":
        if response.POST.get("save"):
            pass
        elif response.POST.get("newItem"):  

    return render(response, 'main/list.html', {"ls":ls})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"] #decryption of the field since we are using post
            t = ToDoList(name = n)
            t.save()

        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(response, 'main/create.html', {"form": form})