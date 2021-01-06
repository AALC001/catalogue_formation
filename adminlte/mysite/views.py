from django.views.generic import CreateView, TemplateView, ListView

from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *


def inscription(request):
    if request.method == 'POST':
        form_iscription = InscriptionForm(request.POST)
        if  form_iscription.is_valid():
            form_iscription.save()
    form_iscription = InscriptionForm()
    return render(request, 'mysite/inscription.html', {'form_iscription' : form_iscription})


def home(request):
    return render(request, 'mysite/home.html')

def catalogue_session(request):
    if request.method == 'POST':
        form_session = SessionForm(request.POST)
        if  form_session.is_valid():
            form_session.save()
    form_session = SessionForm()
    try:
        formation = Formation.objects.all()
    except Formation.DoesNotExist:
        raise Http404("Aucune formation disponible")
    return render(request, 'mysite/session.html', {'formation': formation, 'form_session':form_session})


# def session(request):
#     if request.method == 'POST':
#         form_session = SessionForm(request.POST)
#         if  form_session.is_valid():
#             form_session.save()
#     form_session = SessionForm()
#     return render(request, 'mysite/session.html', {'form_session' : form_session})


def catalogue(request):
    try:
        formation = Formation.objects.all()
    except Formation.DoesNotExist:
        raise Http404("Aucune formation disponible")
    return render(request, 'mysite/catalogue.html', {'formation': formation})


# def session(request):
#     if request.method == 'POST':
#         form_session = SessionForm(request.POST)
#         if form_session.is_valid():
#             date = form_session.cleaned_data['date']
#             heure = form_session.cleaned_data['heure']
#             lieu = form_session.cleaned_data['lieu']
#             capacity = form_session.cleaned_data['capacity']

#     form_session = SessionForm()

#     return render(request, 'mysite/test.html', {'form_session': form_session})
