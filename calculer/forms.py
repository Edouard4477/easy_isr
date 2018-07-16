#Formulaire
from django import forms

class donnees_entree1(forms.Form):
    Date_Inventaire=forms.CharField(max_length=10)

class donnees_entree2(forms.Form):
    age_retr=forms.CharField(max_length=10)

class donnees_entree3(forms.Form):
    #title = forms.CharField(max_length=50)
    file = forms.FileField()
    #Base_Employes=forms.CharField(max_length=300)

choix=('Gabon - Code du travail',
       'Cameroun - Code du travail',
       'Togo - Convention Collective Interprofessionnelle')
class donnees_entree4(forms.Form):
    choix=('Gabon - Code du travail',
       'Cameroun - Code du travail',
       'Togo - Convention Collective Interprofessionnelle')
    Loi=forms.CharField(max_length=300)#, widget=forms.Select(choices=choix))
    #Loi=forms.CharField(max_length=300,
    #                   choices=choix,
    #                    widget=forms.Select(choices=choix),
    #                    )
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
