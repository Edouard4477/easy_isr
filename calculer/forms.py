#Formulaire
from django import forms
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class donnees_entree1(forms.Form):
    Date_Inventaire=forms.CharField(max_length=10)

class donnees_entree2(forms.Form):
    age_retr=forms.CharField(max_length=10)

class donnees_entree3(forms.Form):
    #title = forms.CharField(max_length=50)
    file = forms.FileField()
    #Base_Employes=forms.CharField(max_length=300)

class donnees_entree4(forms.Form):
    list_choix=os.listdir(BASE_DIR+'/calculer/loi')
    choix=[]
    nb_choix=0
    for i in list_choix:
        nb_choix=nb_choix+1

    for i in range(0, nb_choix):
        ligne=[]
        ligne.append(str(list_choix[i]))
        ligne.append(str(list_choix[i]))
        choix.append(ligne)
        
    #choix=(('Gabon - Code du travail','Gabon - Code du travail'),
    #       ('Cameroun - Code du travail','Cameroun - Code du travail'),
    #       ('Togo - Convention Collective Interprofessionnelle','Togo - Convention Collective Interprofessionnelle'))
    #Loi=forms.CharField(max_length=300)#, widget=forms.Select(choices=choix))
    Loi=forms.ChoiceField(widget=forms.Select,choices=choix)
    #Loi=forms.CharField(widget=forms.Select(choices=choix),
    #    )

class donnees_entree5(forms.Form):
    Taux_technique=forms.CharField(max_length=12)

class donnees_entree52(forms.Form):
    Inflation=forms.CharField(max_length=12)

class donnees_entree6(forms.Form):
    Turnover=forms.CharField(max_length=12)

class UploadFileForm(forms.Form):
    #title = forms.CharField(max_length=50)
    file=forms.FileField()
