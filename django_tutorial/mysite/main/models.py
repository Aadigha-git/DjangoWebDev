from django.db import models

# Create your models here.
# essentially creating a database object
class ToDoList(models.Model):
    name = models.CharField(max_length=200)
    #name of attribute = type of field to be stored in DB

    def __str__(self):
        return self.name
    

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    # defines a foreign key relationship between the ToDoItem model and the ToDoList model in Django.
    # cascade delete = If ToDoList is deleted then all items should also be deleted
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text