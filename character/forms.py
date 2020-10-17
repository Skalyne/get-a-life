from django import forms
from .models import MainCharater


class CharacterForm(forms.ModelForm):
    class Meta:
        model = MainCharater
        fields = ('name','last_name','user_character')

        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write yor character name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write yor character last name'}),
            'user_character': forms.TextInput(attrs={'class': 'form-control', 'value': '','id':'elder', 'type': 'hidden',}),

        }