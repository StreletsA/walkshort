from django import forms
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

class LongUrl(forms.Form):
    longurl = forms.CharField(label='Адреc', max_length=100)
