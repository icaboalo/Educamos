from django import forms
from user.models import User


class UserCreationForm(forms.Form):
    full_name = forms.CharField(max_length=50, label='',
                                widget=forms.TextInput(attrs={'placeholder': 'Nombre completo'}))
    username = forms.CharField(max_length=30, label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Usuario'}))
    password = forms.CharField(max_length=30, label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Contraseña'}))
    classroom = forms.IntegerField(label='',
                                   widget=forms.NumberInput(attrs={'placeholder': 'Id unico de salón'}))