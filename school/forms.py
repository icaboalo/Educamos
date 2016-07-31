from django.forms import ModelForm, Form
from django import forms
from audio.models import *

class AudioForm(Form):
    name = forms.CharField(max_length=30, label='', widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    file = forms.FileField(label='')
