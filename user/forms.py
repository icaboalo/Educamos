from django import forms
from user.models import User


class UserCreationForm(forms.Form):
    full_name = forms.CharField(max_length=50, label='',
                                widget=forms.TextInput(attrs={'placeholder': 'Nombre completo', 'class': 'textbox'}))
    username = forms.CharField(max_length=30, label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Usuario', 'class': 'textbox'}))
    password = forms.CharField(max_length=30, label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Contraseña', 'class': 'textbox'}))
    classroom = forms.IntegerField(label='',
                                   widget=forms.NumberInput(attrs={'placeholder': 'Id unico de salón',
                                                                   'class': 'textbox'}))