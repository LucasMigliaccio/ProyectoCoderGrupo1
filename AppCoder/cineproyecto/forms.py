from django import forms

class MoviesForm(forms.Form):

    name = forms.CharField(max_length=30)
    dir = forms.CharField(max_length=30)
    act = forms.CharField(max_length=30)    
    date = forms.DateField()


class UserForm(forms.Form):

    name = forms.CharField(max_length=30)
    surname = forms.CharField(max_length=30)
    user_name = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
    mail = forms.EmailField()
    birth_date = forms.DateField()
    other_info = forms.CharField(max_length=30)