from django import forms

class MoviesForm(forms.Form):

    name = forms.CharField(max_length=30)
    dir = forms.CharField(max_length=30)
    act = forms.CharField(max_length=30)    
    date = forms.DateField()