from django.forms import models
from django.shortcuts import render,redirect
from django.views.generic import CreateView,DeleteView,ListView,UpdateView
from django.urls import reverse_lazy
from .forms import PersonaForm
from .models import Persona

"""
class View()
    dispatch:
    http_not_allowed
"""

class PersonaList(ListView):
    model = Persona
    template_name= 'index.html'

class PersonaCreate(ListView):
    model = Persona
    form_class= PersonaForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('index')

class PersonaUpdate(UpdateView):
    model = Persona
    form_class= PersonaForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('index')

class PersonaDelete(DeleteView):
    model = Persona
    template_name = 'verificacion.html'
    success_url = reverse_lazy('index')