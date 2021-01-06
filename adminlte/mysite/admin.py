from django.contrib import admin
from .models import *


admin.site.site_header = 'CATALOGUE DE FORMATION'
admin.site.site_title = 'Site de formation'

class SessionInline(admin.TabularInline):
    model = Session
    extra = 3

class InscriptionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['nom', 'prenom', 'fonction', 'entreprise', 'email', 'telephone']}),
        ('information1', {'fields': ['formation', 'nb_person', 'session','financement']}),
    ]
    list_display = ['nom', 'prenom', 'fonction', 'entreprise', 'email', 'telephone',#'formation',
     'nb_person', 'session','financement']
    

class FormationAdmin(admin.ModelAdmin):

    fieldsets = [
        (None,               {'fields': ['id_formation']}),
        ('information1', {'fields': ['formation', 'description', 'public','etat',
            'dure', 'thematique',]}),
        ('information2', {'fields': ['profil', 'domaine',
            'presentation', 'objectif',]}),
        ('information3', {'fields': ['pre_requis', 'program', 'modalite']}),
    ]

    inlines = [SessionInline]

    list_display = ['is_actif', 'id_formation', 'formation', 'description', 'public', 'dure', 'thematique',
     'profil', 'domaine', 'presentation', 'objectif','pre_requis', 'program', 'modalite',]

    def is_actif(self, obj):
        return obj.etat == "Oui"
    is_actif.boolean = True



admin.site.register(Inscription, InscriptionAdmin)
admin.site.register(Formation, FormationAdmin)