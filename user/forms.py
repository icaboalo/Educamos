from django import forms
from user.models import User


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'username', 'password', 'classroom']
