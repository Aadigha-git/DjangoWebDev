from django.urls import path

from . import views
# imports view from the current directory we are in

urlpatterns = [
    path("", views.home, name="home"), 
    # If we get into the application and then we are on the homepage --> ""
    # go to views.index has name "index"
    # and we serve the http response index
    path("<int:id>", views.idx, name = "id"),
    path("create/", views.create, name = "create"),
]