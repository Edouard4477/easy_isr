from django.db import models

# Create your models here.

from django import forms
import os
from os import path as os_path
#Pour chargement de fichier
PROJECT_PATH = os.path.abspath(os.path.split(__file__)[0])

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#name=str(request.user)

class Document(models.Model):
    file = models.FileField(upload_to='')#+name)

class DocumentForm(forms.Form):
    file = forms.FileField(label='Selectionner un fichier')
