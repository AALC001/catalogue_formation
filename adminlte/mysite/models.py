from django.db import models
from django.forms import ModelForm



class Formation(models.Model):
    id_formation = models.CharField(max_length=20, primary_key=True, null=False, blank=False)
    formation = models.CharField(max_length=30, null=False, blank=False)
    ACTIF = (
        ('Oui', 'Oui'),
        ('Non', 'Non'),
    )
    etat = models.CharField('Actif', max_length=5, choices=ACTIF)
    description = models.CharField(max_length=100, blank=True, null=True)
    public = models.CharField(max_length=30, blank=True, null=True)
    dure = models.CharField("Durée", max_length=30)
    thematique = models.CharField("thématique", max_length=20, blank=True, null=True)
    profil = models.CharField("Profil utilisateur", max_length=30, blank=True, null=True)
    domaine = models.CharField("Domaine", max_length=30, blank=True, null=True)
    presentation = models.TextField()
    objectif = models.TextField()
    pre_requis = models.TextField()
    program = models.TextField()
    modalite = models.TextField()

    def __str__(self):
        return self.formation


class Inscription(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=100)
    fonction = models.CharField(max_length=30, blank=True, null=True)
    entreprise = models.CharField(max_length=30)
    email = models.EmailField("e-mail", unique=True)
    telephone = models.CharField(max_length=20)
    demande = models.TextField()

    formation = models.ForeignKey(Formation, on_delete=models.PROTECT)
    nb_person = models.PositiveIntegerField("Nombre de personne à former")
    SESSION = (
        ('SESSION JANVIER 2021', 'SESSION JANVIER 2021'),
        ('SESSION FEVRIER 2021', 'SESSION FEVRIER 2021'),
    )
    session = models.CharField("Session de la formation",
            max_length=20, choices=SESSION,)
    FINANCEMENT = (
        ('Entreprise', 'Entreprise'),
        ('Organisme de financement', 'Organisme de financement'),
        ('Personnel', 'Personnel'),
    )
    financement = models.CharField("Financement", max_length=30, choices=FINANCEMENT)

    def __str__(self):
        return self.nom


class Session(models.Model):
    formation = models.ForeignKey(Formation, on_delete=models.PROTECT)
    start_date = models.DateField("Date de debut")
    end_date = models.DateField("Date de fin")
    start_hours = models.TimeField("Heure de debut")
    end_hours = models.TimeField("Heure de fin")
    lieu = models.CharField("Lieu", max_length=50)
    capacity = models.CharField("Capacité d'accueil", max_length=50)
