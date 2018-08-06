from django.shortcuts import render
import datetime
from datetime import datetime
import time
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.views.generic import TemplateView
from django.conf import settings
from .forms import UploadFileForm
from .forms import *
from .models import *
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
from xlwt import easyxf
import xlrd
from xlrd import open_workbook
from xlutils.copy import copy
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
    name=str(request.user)
    chemin_result=BASE_DIR+'/temp_result/'+name
    os.makedirs(chemin_result, mode=0o777, exist_ok=True)
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

def handle_uploaded_file(f,name):
    with open(BASE_DIR+'/temp_result/'+name+'/salaries.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def handle_xls(f):
    with open(BASE_DIR+'/salaries.txt', 'wb+') as destination:
        wb=open_workbook(f)#second bug
        sh=wb.sheet_by_name(u'Feuil1')
        salarie=[]
        nb_salarie=sh.nrows
        for rownum in range(sh.nrows):
            salarie.append(sh.row_values(rownum))
        for i in range(0, nb_salarie):
            for j in range(0, 3):
                destination.write(str(salarie[i][j]))

def entree3(request):
    if request.method=='POST':
        form=UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            name=str(request.user)
            handle_uploaded_file(request.FILES['file'], name)
            #print(form)
            fic_employes='/temp_result/'+name+'/salaries.txt'
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
          print(form.errors)
    else:
        form=UploadFileForm()
    #documents=Document.objects.all()
    #return render_to_response('saisie3.html',
    #                          {'documents': documents, 'form': form},
    #                          context_instance=RequestContext(request)
    #                          )
    return render(request,'saisie3.html',
                  {'form': form}
                  )#locals())

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
            
            return HttpResponseRedirect('/inflation')
    else:
        form=donnees_entree5()
    return render(request,'saisie5.html',locals())

def entree52(request):
    if request.method=='POST':
        form=donnees_entree52(request.POST)
        if form.is_valid():
            infl=form.cleaned_data['Inflation']
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
            fic=open(chemin_result+'/'+'Simulation'+'.txt','w')
            fic.write(Date_inv+'\n'+age_retr+'\n')
            fic.write(fic_employes)
            fic.write('\n')
            fic.write(loi)
            fic.write('\n')
            fic.write(tech)
            fic.write('\n')
            fic.write(infl)
            fic.close()
            
            return HttpResponseRedirect('/turnover')
    else:
        form=donnees_entree52()
    return render(request,'saisie52.html',locals())

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
            infl=sim[5][0]
            os.makedirs(chemin_result+'/'+Date_inv+'/'+tech+'/'+to, mode=0o777, exist_ok=True)
            fic=open(chemin_result+'/'+'Simulation'+'.txt','w')
            fic.write(Date_inv+'\n'+age_retr+'\n')
            fic.write(fic_employes)
            fic.write('\n')
            fic.write(loi)
            fic.write('\n')
            fic.write(tech)
            fic.write('\n')
            fic.write(infl)
            fic.write('\n')
            fic.write(to)
            fic.close()
            #fic_employes=chemin_result+'/'+Date_inv+'/Liste_salarie1.xlsx'
            r=open(chemin_result+'/'+Date_inv+'/'+tech+'/'+to+'/run.txt','w')
            r.write('1')
            r.write('\n')
            r.write('100')#modifier pas
            r.close()
            return HttpResponseRedirect('/Attente')
    else:
        form=donnees_entree6()
    return render(request,'saisie6.html',locals())

def attente(request):
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
    infl=sim[5][0]
    to=sim[6][0]
    fic_employes=BASE_DIR+fic_employes
    f=open(fic_employes,'r')
    li=f.readlines()
    nb_salarie=0
    for i in li:
        r=i.strip('\n')
        v=r.split('\t')
        nb_salarie=nb_salarie+1

    nb_salarie=nb_salarie-1
    f=open(chemin_result+'/'+Date_inv+'/'+tech+'/'+to+'/run.txt','r')
    li=f.readlines()
    run=[]
    for i in li:
        r=i.strip('\n')
        v=r.split('\t')
        run.append(v)
        
    debut=int(run[0][0])
    fin=int(run[1][0])
    if debut==1:
        prov_vie=0
        prov_deces=0
        masse=0
        nb_employe=0
        pyr=zeros(shape=(100,1))
        dur=zeros(shape=(50,2))
    if debut>1:
        f=open(chemin_result+'/'+Date_inv+'/'+tech+'/'+to+'/resultats.txt','r')
        li=f.readlines()
        result=[]
        for i in li:
            r=i.strip('\n')
            v=r.split('\t')
            result.append(v)
        prov_vie=float(result[0][0])
        prov_deces=float(result[1][0])
        masse=float(result[2][0])
        nb_employe=int(result[3][0])

        f=open(chemin_result+'/'+Date_inv+'/'+tech+'/'+to+'/pyramide.txt','r')
        li=f.readlines()
        pyr=[]
        l=0
        for i in li:
            r=i.strip('\n')
            v=r.split('\t')
            pyr.append(v)
            l=l+1
        for i in range(0, l):
            pyr[i][0]=float(pyr[i][0])

        f=open(chemin_result+'/'+Date_inv+'/'+tech+'/'+to+'/duration.txt','r')
        li=f.readlines()
        dur=[]
        lo=0
        for i in li:
          r=i.strip('\n')
          v=r.split('\t')
          dur.append(v)
          lo=lo+1
        for i in range(0, lo):
          dur[i][0]=float(dur[i][0])
          dur[i][1]=float(dur[i][1])
            
        
    if fin >= nb_salarie:
        fin=nb_salarie
        
    prov=isr(Date_inv,age_retr,fic_employes,loi,tech,infl,to,debut,fin)
    r=open(chemin_result+'/'+Date_inv+'/'+tech+'/'+to+'/resultats.txt','w')
    r.write(str(prov_vie+prov[0]))
    r.write('\n')
    r.write(str(prov_deces+prov[1]))
    r.write('\n')
    r.write(str(masse+prov[2]))
    r.write('\n')
    r.write(str(prov[3]))
    pyr2=prov[5]
    print(pyr2)
    l=len(pyr2)
    p=open(chemin_result+'/'+Date_inv+'/'+tech+'/'+to+'/pyramide.txt','w')
    for i in range(0,l):
        p.write(str(pyr[i][0]+pyr2[i][1]))
        p.write('\n')
    p.close()

    p=open(chemin_result+'/'+Date_inv+'/'+tech+'/'+to+'/duration.txt','w')
    duration=prov[6]
    for i in range(0,50):
      p.write(str(dur[i][0]+duration[i][0]))
      p.write('\t')
      p.write(str(dur[i][1]+duration[i][1]))
      if i<49:
        p.write('\n')
    p.close()
    if fin<nb_salarie:
        r=open(chemin_result+'/'+Date_inv+'/'+tech+'/'+to+'/run.txt','w')
        r.write(str(fin))
        r.write('\n')
        r.write(str(fin+100))#100 - modifier pas
        r.close()
        ratio=int(fin/nb_salarie*100)
        return render(request, 'attente.html',{'ratio':ratio})#HttpResponseRedirect('/Attente')#render(request, 'attente.html',{'fin':fin})

    if fin==nb_salarie:
        return HttpResponseRedirect('/Result')

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
    infl=sim[5][0]
    to=sim[6][0]
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
    vie=float(vie)
    deces=float(deces)
    masse=float(masse)
    ratio=vie/masse
    vie_form=affiche(vie)
    deces_form=affiche(deces)
    masse=affiche(masse)
    pyr_age=zeros(shape=(2,100))
    for i in range(0,100):
        pyr_age[0][i]=i
    x=pyr_age[0]
    f=open(chemin_result+'duration.txt')
    li=f.readlines()
    dur=[]
    nb_li=0
    for i in li:
      r=i.strip('\n')
      v=r.split('\t')
      dur.append(v)
      nb_li=nb_li+1
    dur_vie=zeros(shape=(50,1))
    dur_deces=zeros(shape=(50,1))
    for i in range(0,nb_li):
      dur_vie[i][0]=float(dur[i][0])
      dur_deces[i][0]=float(dur[i][1])

    dur_vie_ta=zeros(shape=(11,1))
    dur_deces_ta=zeros(shape=(11,1))
    for i in range(0,11):
      if i<10:
        dur_vie_ta[i][0]=dur_vie[i][0]
        dur_deces_ta[i][0]=dur_deces[i][0]
      if i==10:
        for j in range(10,50):
          dur_vie_ta[i][0]=dur_vie_ta[i][0]+dur_vie[j][0]
          dur_deces_ta[i][0]=dur_deces_ta[i][0]+dur_deces[j][0]
    dur_vie_tab=[]
    dur_deces_tab=[]
    for i in range(0,11):
      dur_vie_tab.append(affiche(dur_vie_ta[i][0]/1000))
      dur_deces_tab.append(affiche(dur_deces_ta[i][0]/1000))
    xa=zeros(shape=(1,50))
    cumul_vie=zeros(shape=(1,50))
    cumul_deces=zeros(shape=(1,50))
    for i in range(0,50):
      xa[0][i]=i
      for j in range(0,i+1):
        cumul_vie[0][i]=cumul_vie[0][i]+dur_vie[j][0]
        cumul_deces[0][i]=cumul_deces[0][i]+dur_deces[j][0]
    
    title2='Duration'
    plot2=figure(title=title2,
                x_axis_label='Année',
                y_axis_label='Cumul des engagements',
                plot_width=1200,
                plot_height=400)
    plot2.line(xa[0], cumul_vie[0], color="green", legend="en cas de vie")
    plot2.line(xa[0], cumul_deces[0], color="#feb24c", legend="en cas de décès")
    script2, div2=components(plot2)
    
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
                x_axis_label='Nombre',
                y_axis_label='Age',
                plot_width=1200,
                plot_height=400)
    
    plot.hbar(x, height=1, left=0, right=y, name='Salariés', legend='Salariés', color="#40A497")
    script, div = components(plot)
    to = float(to)
    to=to*100
    to=str(to)+'%'
    infl=float(infl)
    infl=infl*100
    infl=str(infl)+'%'
    ratio=float(ratio)
    ratio=ratio*10000
    ratio=int(ratio)
    ratio=float(ratio/100)
    ratio=str(ratio)+'%'
    prop=readlaw(loi)[0]
    taux=readlaw(loi)[1]
    taux=int(taux*100)
    taux=str(taux)+'%'
    table=readlaw(loi)[7]
    table2=[]
    abdc1=0
    abdc2=0
    print(prop+1)
    if prop==3:
      table2=retire(loi)
      abdc1=str(abondeces(loi)[0])
      abdc2=str(abondeces(loi)[1])
    print(dur)
    print(dur_vie)
    print(dur_vie_tab)
    loi2=''
    top=0
    for i in range(0,300):
      if top==0:
        loi2=loi2+loi[i:i+1]
      if loi[i:i+1]=='-':
        top=1
    print(table)
    loi_mimi=loi
    loi3=loi2+' Convention Collective Interprofessionnelle'
    loi2=loi2+' Code du travail'
    print(loi2)
    print(loi3)
    if os.path.isdir(BASE_DIR+'/calculer/loi/'+loi2+'/')==True:
      loi_mini=loi2
    if os.path.isdir(BASE_DIR+'/calculer/loi/'+loi3+'/')==True:
      loi_mini=loi3
    print(loi_mini)
    table_min=readlaw(loi_mini)[7]
    l=len(table)
    for i in range(0,l):
      if i>0:
        table[i][0]=table[i][0]-1

    l=len(table_min)
    for i in range(0,l):
      if i>0:
        table_min[i][0]=table_min[i][0]-1
    return render(request, 'result.html',{'loi_mini':loi_mini,'table_min':table_min,'abdc1':abdc1,'abdc2':abdc2,'table2':table2,'script2':script2,'div2':div2,'dur_vie_tab':dur_vie_tab,'dur_deces_tab':dur_deces_tab,'prop':prop,'taux':taux,'table':table,'age_moy':age_moy,'infl':infl,'script':script,'div':div,'vie_form':vie_form,'deces_form':deces_form, 'ratio':ratio, 'Date_inv':Date_inv, 'loi':loi, 'tech':tech, 'to':to, 'masse':masse, 'effectif':effectif})


