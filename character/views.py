from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from .models import MainCharater
from .forms import CharacterForm

# Create your views here.


class AddCharacterView(CreateView):
    model = MainCharater

    form_class = CharacterForm
    template_name = "create_character.html"


class HomeView(ListView):
    model = MainCharater
    template_name = 'index.html'

    def get_context_data(self,*args,**kwargs):
        life_characters = MainCharater.objects.filter(user_character = 1)
        context = super(HomeView, self).get_context_data(*args,**kwargs)
        context['life_charaters']= life_characters

        return context


