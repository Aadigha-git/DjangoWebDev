from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.

def home(response):
    return render(response, 'main/home.html', {})

def idx(response, id):
    ls = ToDoList.objects.get(id=id)
    if ls in response.user.todolist.all():
        #item = ls.item_set.get(id = id)
        #{"save": ["save"], "c1":["clicked"]} #name save points to the value save
        if response.method == "POST":
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c"+ str(item.id)) == "clicked":       #saving the check buttons
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()
            elif response.POST.get("newItem"):
                txt = response.POST.get("new")
                if len(txt) > 2 and len(txt) < 201:
                    ls.item_set.create(text = txt, complete=False)
                else:
                    print("Invalid input. character size 3 to 200")

        return render(response, 'main/list.html', {"ls":ls})
    return render(response, 'main/view.html', {})
def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"] #decryption of the field since we are using post
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)


        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(response, 'main/create.html', {"form": form})

def view(response):
    return render(response, "main/view.html", {})