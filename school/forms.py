from django import forms

class AudioForm(forms.Form):
    file = forms.FileField()
    name = forms.CharField(max_length=30)
