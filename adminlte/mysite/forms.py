from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

from .models import *



class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Inscription
        fields = ['nom', 'prenom', 'fonction', 'entreprise', 'email', 'telephone', 'formation', 'nb_person', 'session','financement']


class FormationForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = ['id_formation', 'formation', 'description', 'public', 'etat',
            'dure', 'thematique', 'profil', 'domaine',
            'presentation', 'objectif', 'pre_requis', 'program', 'modalite']


class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['start_date', 'end_date', 'start_hours', 'end_hours', 'lieu', 'capacity',]


class PriseContactForm(forms.ModelForm):
    class Meta:
        model = Inscription
        fields = ['nom', 'prenom', 'fonction', 'entreprise', 'email', 'telephone', 'demande']


# class DateWidget(forms.MultiWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__([
#             forms.DateInput(attrs={'type':'date'}),
#             forms.DateInput(),
#         ], attrs)

#     def decompress(self, value):
#         if value:
#             return value.split('')
#         return['', '']


# class DateFields(forms.MultiValueField):

#     widget = DateWidget

#     def __init__(self, *args, **kwargs):
#         fiels = (
#             forms.DateField(),
#             forms.DateField(),
#         )

#         super().__init__(self, *args, **kwargs)

#     def compress(self, data_list):
#         return f'{data_list[0]} {data_list[1]}'


# class SessionForm(forms.Form):
#     date = forms.DateField()
#     heure = forms.TimeField()
#     lieu = forms.CharField()
#     capacity = forms.CharField(label="Capacité d'accueil")

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         self.helper = FormHelper
#         self.helper.form_method = 'post'

#         self.helper.layout = Layout(
#             'date', 'heure', 'lieu', 'capacity',
#             Submit('submit', 'Submit', css_class='btn-success')
#         )