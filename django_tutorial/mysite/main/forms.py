from django import forms

class CreateNewList(forms.Form):
    # these fields are the same fields in your database 
    # https://docs.djangoproject.com/en/4.2/intro/tutorial04/

    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)
