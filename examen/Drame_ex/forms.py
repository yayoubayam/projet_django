from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Tâche
from .models import User

class UserForm(forms.ModelForm):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    # email = forms.CharField(label="Email d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    class Meta :
        model = User
        fields=["username","password"]

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tâche
        fields = "__all__"
        exclude = []
    # title = forms.CharField(
    # 	widget=forms.TextInput(
    # 		attrs={
    # 		"class": "form-control form-control-lg",
    # 		"placeholder": "Nouvelle tâche ...",
    # 		}),)          


class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)