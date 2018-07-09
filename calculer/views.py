from django.shortcuts import render
import datetime
from datetime import datetime
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.views.generic import TemplateView
from django.conf import settings
from .forms import UploadFileForm
from .forms import *
from django import forms
from django.shortcuts import render_to_response
from django.template import RequestContext

from calculer import *
from .calcul import *

import os
from numpy import *
from django.http import JsonResponse
from django.views.generic import View
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
# Create your views here.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class LoginView(TemplateView):

  template_name = 'front/index.html'
  date=datetime.now()

  def post(self, request, **kwargs):

    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        return HttpResponseRedirect('/isr')#settings.LOGIN_REDIRECT_URL )

    return render(request, self.template_name,{'date':date})


class LogoutView(TemplateView):

  template_name = 'front/index.html'
  date=datetime.now()

  def get(self, request, **kwargs):

    logout(request)

    return render(request, self.template_name,{'date':date})


def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    date=datetime.now()
    name=request.user
    print(name)
    return render(request, 'index.html',{'date': date,'name': name})

def entree(request):
    if request.method=='POST':
        form=donnees_entree1(request.POST)
        if form.is_valid():
            Date_inv=form.cleaned_data['Date_Inventaire']
            #Risque=form.cleaned_data['Risque']
            #fic_sinistre=form.cleaned_data['Base_Sinistres']
            #tx_actu=form.cleaned_data['Taux_actualisation']
            name=str(request.user)
            chemin_result=BASE_DIR+'/temp_result/'+name
            os.makedirs(chemin_result, mode=0o777, exist_ok=True)
            fic=open(chemin_result+'/'+'Simulation'+'.txt','w')
            fic.write(Date_inv)
            fic.close()
            os.makedirs(chemin_result+'/'+Date_inv, mode=0o777, exist_ok=True)
            
            return HttpResponseRedirect('/age_retraite')
    else:
        form=donnees_entree1()
    return render(request,'saisie.html',locals())

def entree2(request):
    if request.method=='POST':
        form=donnees_entree2(request.POST)
        if form.is_valid():
            age_retr=form.cleaned_data['age_retr']
            name=str(request.user)
            chemin_result=BASE_DIR+'/temp_result/'+name
            f=open(chemin_result+'/Simulation.txt','r')
            li=f.readlines()
            sim=[]
            nb_contrat=0
            for i in li:
                r=i.strip("\n")
                v=r.split('\t')
                sim.append(v)
            Date_inv=sim[0][0]
            fic=open(chemin_result+'/'+'Simulation'+'.txt','w')
            fic.write(Date_inv+'\n'+age_retr)
            fic.close()
            os.makedirs(chemin_result+'/'+Date_inv+'/'+age_retr, mode=0o777, exist_ok=True)
            
            return HttpResponseRedirect('/employes')
    else:
        form=donnees_entree2()
    return render(request,'saisie2.html',locals())

def entree3(request):
    if request.method=='POST':
        form=donnees_entree3(request.POST)
        if form.is_valid():
            fic_employes=form.cleaned_data['Base_Employes']
            name=str(request.user)
            chemin_result=BASE_DIR+'/temp_result/'+name
            f=open(chemin_result+'/Simulation.txt','r')
            li=f.readlines()
            sim=[]
            nb_contrat=0
            for i in li:
                r=i.strip("\n")
                v=r.split('\t')
                sim.append(v)
            Date_inv=sim[0][0]
            age_retr=sim[1][0]
            fic=open(chemin_result+'/'+'Simulation'+'.txt','w')
            fic.write(Date_inv+'\n'+age_retr+'\n')
            fic.write(fic_employes)
            fic.close()
            
            return HttpResponseRedirect('/loi')
    else:
        form=donnees_entree3()
    return render(request,'saisie3.html',locals())

def entree4(request):
    if request.method=='POST':
        form=donnees_entree4(request.POST)
        if form.is_valid():
            loi=form.cleaned_data['Loi']
            name=str(request.user)
            chemin_result=BASE_DIR+'/temp_result/'+name
            f=open(chemin_result+'/Simulation.txt','r')
            li=f.readlines()
            sim=[]
            nb_contrat=0
            for i in li:
                r=i.strip("\n")
                v=r.split('\t')
                sim.append(v)
            Date_inv=sim[0][0]
            age_retr=sim[1][0]
            fic_employes=sim[2][0]
            fic=open(chemin_result+'/'+'Simulation'+'.txt','w')
            fic.write(Date_inv+'\n'+age_retr+'\n')
            fic.write(fic_employes)
            fic.write('\n')
            fic.write(loi)
            fic.close()
            
            return HttpResponseRedirect('/tech')
    else:
        form=donnees_entree4()
    return render(request,'saisie4.html',locals())

def entree5(request):
    if request.method=='POST':
        form=donnees_entree5(request.POST)
        if form.is_valid():
            tech=form.cleaned_data['Taux_technique']
            name=str(request.user)
            chemin_result=BASE_DIR+'/temp_result/'+name
            f=open(chemin_result+'/Simulation.txt','r')
            li=f.readlines()
            sim=[]
            nb_contrat=0
            for i in li:
                r=i.strip("\n")
                v=r.split('\t')
                sim.append(v)
            Date_inv=sim[0][0]
            age_retr=sim[1][0]
            fic_employes=sim[2][0]
            loi=sim[3][0]
            fic=open(chemin_result+'/'+'Simulation'+'.txt','w')
            fic.write(Date_inv+'\n'+age_retr+'\n')
            fic.write(fic_employes)
            fic.write('\n')
            fic.write(loi)
            fic.write('\n')
            fic.write(tech)
            fic.close()
            
            return HttpResponseRedirect('/turnover')
    else:
        form=donnees_entree5()
    return render(request,'saisie5.html',locals())

def entree6(request):
    if request.method=='POST':
        form=donnees_entree6(request.POST)
        if form.is_valid():
            to=form.cleaned_data['Turnover']
            name=str(request.user)
            chemin_result=BASE_DIR+'/temp_result/'+name
            f=open(chemin_result+'/Simulation.txt','r')
            li=f.readlines()
            sim=[]
            nb_contrat=0
            for i in li:
                r=i.strip("\n")
                v=r.split('\t')
                sim.append(v)
            Date_inv=sim[0][0]
            age_retr=sim[1][0]
            fic_employes=sim[2][0]
            loi=sim[3][0]
            tech=sim[4][0]
            os.makedirs(chemin_result+'/'+Date_inv+'/'+tech+'/'+to, mode=0o777, exist_ok=True)
            fic=open(chemin_result+'/'+'Simulation'+'.txt','w')
            fic.write(Date_inv+'\n'+age_retr+'\n')
            fic.write(fic_employes)
            fic.write('\n')
            fic.write(loi)
            fic.write('\n')
            fic.write(tech)
            fic.write('\n')
            fic.write(to)
            fic.close()
            prov=isr(Date_inv,age_retr,fic_employes,loi,tech,to)
            r=open(chemin_result+'/'+Date_inv+'/'+tech+'/'+to+'/resultats.txt','w')
            r.write(str(prov[0]))
            r.write('\n')
            r.write(str(prov[1]))
            r.write('\n')
            r.write(str(prov[2]))
            r.write('\n')
            r.write(str(prov[3]))
            r.write('\n')
            r.write(str(prov[4]))
            r.close()
            pyr=prov[5]
            print(pyr)
            l=len(pyr)
            p=open(chemin_result+'/'+Date_inv+'/'+tech+'/'+to+'/pyramide.txt','w')
            for i in range(0,l):
                p.write(str(pyr[i][1]))
                p.write('\n')
            p.close()
            return HttpResponseRedirect('/Result')
    else:
        form=donnees_entree6()
    return render(request,'saisie6.html',locals())

def sortie(request):
    name=str(request.user)
    chemin_result=BASE_DIR+'/temp_result/'+name
    f=open(chemin_result+'/Simulation.txt','r')
    li=f.readlines()
    sim=[]
    for i in li:
        r=i.strip("\n")
        v=r.split('\t')
        sim.append(v)
    Date_inv=sim[0][0]
    age_retr=sim[1][0]
    fic_employes=sim[2][0]
    loi=sim[3][0]
    tech=sim[4][0]
    to=sim[5][0]
    chemin_result=chemin_result+'/'+Date_inv+'/'+tech+'/'+to+'/'
    #os.startfile(chemin_result+'TFA.txt')
    f=open(chemin_result+'resultats.txt')
    li=f.readlines()
    result=[]
    nb_ligne=0
    for i in li:
        r=i.strip("\n")
        v=r.split('\t')
        result.append(v)
    vie=result[0][0]
    deces=result[1][0]
    masse=result[2][0]
    effectif=result[3][0]
    ratio=result[4][0]
    vie=float(vie)
    deces=float(deces)
    masse=float(masse)
    vie_form=affiche(vie)
    deces_form=affiche(deces)
    masse=affiche(masse)
    pyr_age=zeros(shape=(2,100))
    for i in range(0,100):
        pyr_age[0][i]=i
    x=pyr_age[0]
    f=open(chemin_result+'pyramide.txt')
    li=f.readlines()
    pyr=[]
    nb_l=0
    for i in li:
        r=i.strip("\n")
        v=r.split('\t')
        nb_l=nb_l+1
        pyr.append(v)
    for i in range(0,nb_l):
        pyr_age[1][i]=float(pyr[i][0])

    y=pyr_age[1]
    age_moy=0
    nb=0
    for i in range(0,nb_l):
        nb=nb+y[i]
        age_moy=age_moy+x[i]*y[i]

    age_moy=age_moy/nb
    age_moy=int(age_moy*100)/100
    title='Pyramide des âges - Salariés'
    plot=figure(title=title,
                x_axis_label='Age',
                y_axis_label='Nombre',
                plot_width=1200,
                plot_height=400)
    
    plot.hbar(x, height=1, left=0, right=y, name='Salariés', legend='Salariés', color="#40A497")
    script, div = components(plot)
    to = float(to)
    to=to*100
    to=str(to)+'%'
    ratio=float(ratio)
    ratio=ratio*10000
    ratio=int(ratio)
    ratio=float(ratio/100)
    ratio=str(ratio)+'%'
    prop=readlaw(loi)[0]
    taux=readlaw(loi)[1]
    taux=int(taux*100)
    taux=str(taux)+'%'
    table=readlaw(loi)[3]
    return render(request, 'result.html',{'prop':prop,'taux':taux,'table':table,'age_moy':age_moy,'script':script,'div':div,'vie_form':vie_form,'deces_form':deces_form, 'ratio':ratio, 'Date_inv':Date_inv, 'loi':loi, 'tech':tech, 'to':to, 'masse':masse, 'effectif':effectif})

