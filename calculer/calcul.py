import numpy
from numpy import *
import scipy
from scipy import *
from datetime import *
import matplotlib
from matplotlib import *
import sys
from sys import *
import os
from xlwt import easyxf
import xlrd
from xlrd import open_workbook
from xlutils.copy import copy

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#Futurs variable d'entrée
        

def affiche(valeur):#Fonction d'affichage des valeurs avec espace tous les milliers
    if valeur>=1e9:
        affiche=str(int(valeur/1e9))
        million=str(int(int(valeur/1e6)-int(valeur/1e9)*1e3))
        if(int(million)<1):
            million='000'
        elif(int(million)<10):
            million='00'+million
        elif(int(million)<100):
            million='0'+million
        else:
            million=million
        millier=str(int(int(valeur/1e3)-int(valeur/1e6)*1e3))
        if(int(millier)<1):
           millier='000'
        elif(int(millier)<10):
            millier='00'+millier
        elif(int(millier)<100):
            millier='0'+millier
        else:
            millier=millier
        unite=str(int(int(valeur)-int(valeur/1e3)*1e3))
        if(int(unite)<1):
           unite='000'
        elif(int(unite)<10):
            unite='00'+unite
        elif(int(unite)<100):
            unite='0'+unite
        else:
            unite=unite
        affiche=affiche+" "+million+" "+millier+" "+unite
    if valeur<1e9 and valeur>=1e6:
        affiche=str(int(valeur/1e6))
        millier=str(int(int(valeur/1e3)-int(valeur/1e6)*1e3))
        if(int(millier)<1):
           millier='000'
        elif(int(millier)<10):
            millier='00'+millier
        elif(int(millier)<100):
            millier='0'+millier
        else:
            millier=millier
        unite=str(int(int(valeur)-int(valeur/1e3)*1e3))
        if(int(unite)<1):
           unite='000'
        elif(int(unite)<10):
            unite='00'+unite
        elif(int(unite)<100):
            unite='0'+unite
        else:
            unite=unite
        affiche=affiche+" "+millier+" "+unite
    if valeur<1e6 and valeur>=1e3:
        affiche=str(int(valeur/1e3))
        unite=str(int(int(valeur)-int(valeur/1e3)*1e3))
        if(int(unite)<1):
           unite='000'
        elif(int(unite)<10):
            unite='00'+unite
        elif(int(unite)<100):
            unite='0'+unite
        else:
            unite=unite
        affiche=affiche+" "+unite
    if valeur<1e3:
        affiche=int(valeur)
    return(affiche)

def affiche_millions(valeur):
    affiche=str(int(valeur/1e9))
    million=str(int(int(valeur/1e6)-int(valeur/1e9)*1e3))
    if (affiche=='0'):
        if(int(million)<1):
            million='  -   '
        elif(int(million)<10):
            million='  '+million
        elif(int(million)<100):
            million=' '+million
        else:
            million=million
    if (affiche!='0'):    
        if(int(million)<1):
            million='000'
        elif(int(million)<10):
            million='00'+million
        elif(int(million)<100):
            million='0'+million
        else:
            million=million
    if (affiche!='0'):
        affiche=affiche+' '+million
    if (affiche=='0'):
        affiche='   '+million
    return(affiche)

def addmonth(date,n):
    j=date.day
    m=date.month
    a=date.year
    if m+n>12:
        a=a+int((m+n-1)/12)
        m=(m+n)%12
        if m==0:
            m=12
    else:
        m=m+n
    date=datetime(a,m,j)
    return(date)
    
def convert(date):
    j=int(date[0:2])
    m=int(date[3:5])
    a=int(date[6:10])
    #date=m
    date=datetime(a,m,j)
    return(date)

def convert2(date):
    j=int(date[0:1])
    m=int(date[2:3])
    a=int(date[4:8])
    #date=m
    date=datetime(a,m,j)
    return(date)

def convert_int(val):
    val=val.replace(',','.')
    val=float(val)
    val=int(val)
    return(val)

def convert_float(val):
    val=val.replace(',','.')
    val=float(val)
    return(val)

def nb_year(val):
    val=val.total_seconds()
    val=val/(365.25*24*60*60)
    return(val)


def pcent(val):
    val=val.replace('%','')
    val=val.replace(',','.')
    val=float(val)
    val=val/100
    return(val)

def convert_xls(date):
    date=int(date)
    date2=datetime(1899,12,30)+timedelta(date)
    date=date2
    return(date)

def max(a,b):
    if a>b:
        c=a
    if a<=b:
        c=b
    return(c)

def readlaw(loi):
    loi=str(loi)
    chemin=BASE_DIR+'/calculer/loi/'
    filepath=chemin+loi+'/loi.txt'
    f=open(filepath,"r")
    law=[]
    nb_l=0
    li=f.readlines()
    for i in li:
        r=i.strip("\n")
        v=r.split('\t')
        nb_l=nb_l+1
        law.append(v)
    ratio=0.0
    law[1][1]=int(law[1][1])
    law[2][1]=float(law[2][1])
    law[3][1]=int(law[3][1])
    prop=law[1][1]
    x = law[2][1]
    giedeces=law[3][1]
    mini=float(law[4][1])
    maxi=int(law[6][1])
    mt_mini=int(law[5][1])
    mt_maxi=int(law[7][1])
    table=zeros(shape=(nb_l-9,3))
    for i in range(9,nb_l):
        for j in range(0,3):
            table[i-9][j]=float(law[i][j])
    
    return(prop, x, giedeces,mini,mt_mini,maxi,mt_maxi,table)

def retire(loi):
    loi=str(loi)
    chemin=BASE_DIR+'/calculer/loi/'
    filepath=chemin+loi+'/retraite.txt'
    f=open(filepath,"r")
    retir=[]
    nb_l=0
    li=f.readlines()
    for i in li:
        r=i.strip('\n')
        v=r.split('\t')
        nb_l=nb_l+1
        retir.append(v)
    nb_c=0
    for i in retir[3]:
        nb_c=nb_c+1
    table=zeros(shape=(nb_l,nb_c))
    for i in range(0,nb_l):
        for j in range(0,nb_c):
            table[i][j]=float(retir[i][j])
    return(table)

def abondeces(loi):
    loi=str(loi)
    chemin=BASE_DIR+'/calculer/loi/'
    filepath=chemin+loi+'/deces.txt'
    f=open(filepath,"r")
    abond=[]
    nb_l=0
    li=f.readlines()
    for i in li:
        r=i.strip('\n')
        v=r.split('\t')
        nb_l=nb_l+1
        abond.append(v)
    freq=float(abond[1][1])
    plaf=float(abond[2][1])
    return(freq,plaf)
    
def droit(table,x):
    y=0
    x2=int(x)
    l=len(table)
    for i in range(1,x2+1):
        for j in range(0,l):
            if table[j][0]-1<i and table[j][1]>=i:
                y=y+table[j][2]
    for j in range(0,l):
        if x2>table[j][0]-1 and x2<=table[j][1]:
            y=y+table[j][2]*(x-x2)
    return(y)

def droit2(table,x,y):
    z=0.0
    x2=int(x)
    l=len(table)
    larg=0
    if x>table[l-1][0]:
        x=table[l-1][0]
    for i in table[0]:
        larg=larg+1
    for i in range(1,l):
        if table[i][0]==x:
            for j in range(1,larg):
                if y<=table[0][j] and y>table[0][j-1]:
                    z=table[i][j]
    return(z)

#Calcul ISR
def isr(date_inv, age_retr, filepath, loi, tech, infl, to, debut, fin):
    #chemin='C:/Users/Saontsy/Desktop/Arrete 31122017/Calcul ISR/'
    Tvie=BASE_DIR+'/calculer/Table_mortalité/CIMAF.txt'
    Tmort=BASE_DIR+'/calculer/Table_mortalité/CIMAH.txt'
    prop=readlaw(loi)[0]#1er bug
    #taux=0.2#étudier tous les codes du travail et convention collectives
    giedeces=1
    to=float(to)
    annee_inv=date_inv[6:10]
    annee_inv=int(annee_inv)
    date_inv=convert(date_inv)
    age_retr=int(age_retr)
    tech=float(tech)
    infl=float(infl)
    mini=readlaw(loi)[3]
    mt_mini=readlaw(loi)[4]
    maxi=readlaw(loi)[5]
    mt_maxi=readlaw(loi)[6]
    duration=zeros(shape=(50,2))
        
    f=open(Tvie,"r")
    li=f.readlines()
    lx=[]
    for i in li:
        r=i.strip("\n")
        v=r.split('\t')
        lx.append(v)

    nb_lx=0
    for i in lx:
        nb_lx=nb_lx+1

    for i in range(1, nb_lx):
        lx[i][0]=int(lx[i][0])
        lx[i][1]=lx[i][1].replace(',','.')
        lx[i][1]=float(lx[i][1])

    f=open(Tmort,"r")
    li=f.readlines()
    ly=[]
    for i in li:
        r=i.strip("\n")
        v=r.split('\t')
        ly.append(v)

    nb_ly=0
    for i in ly:
        nb_ly=nb_ly+1

    for i in range(1, nb_ly):
        ly[i][0]=int(ly[i][0])
        ly[i][1]=ly[i][1].replace(',','.')
        ly[i][1]=float(ly[i][1])

    #wb=open_workbook(filepath)#second bug
    #sh=wb.sheet_by_name(u'Feuil1')
    salarie=[]
    #nb_salarie=sh.nrows
    #for rownum in range(sh.nrows):
    #    salarie.append(sh.row_values(rownum))    
    nb_salarie=0
    #filepath=BASE_DIR+filepath - enlevé pour partition du calcul
    print(filepath)
    f=open(filepath,"r")
    li=f.readlines()
    for i in li:
        r=i.strip("\n")
        v=r.split('\t')
        nb_salarie=nb_salarie+1
        salarie.append(v)

    print(nb_salarie)
    nb_salarie=nb_salarie-1
    for i in range(1, nb_salarie):
        salarie[i][0]=int(salarie[i][0])
        salarie[i][1]=convert(salarie[i][1])
        salarie[i][2]=convert(salarie[i][2])
        salarie[i][3]=convert_float(salarie[i][3])
        #salarie[i][1]=convert_xls(salarie[i][1]) - pour fichier excel
        #salarie[i][2]=convert_xls(salarie[i][2]) - pour fichier excel
        #salarie[i][3]=float(salarie[i][3]) - pour fichier excel
        
    prov_dc=zeros(shape=(nb_salarie,1))
    prov_lf=zeros(shape=(nb_salarie,1))

    prov_vie=0
    prov_deces=0
    masse=0
    pyr=zeros(shape=(100,2))
    for i in range(0,100):
        pyr[i][0]=i
    for i in range(debut, fin):
        age=0
        age=annee_inv-salarie[i][1].year
        for j in range(0,100):
            if age==pyr[j][0]:
                pyr[j][1]=pyr[j][1]+1
    
    if prop==2:
        table=readlaw(loi)[7]
        print(table)
        for i in range(debut, fin):
            age=0
            age=annee_inv-salarie[i][1].year
            anc=(date_inv-salarie[i][2]).days/365.25
            depart_retr=datetime(salarie[i][1].year+age_retr, salarie[i][1].month, 1)
            anc_proj=max((depart_retr-salarie[i][2]).days/365.25,anc)
            dt=(depart_retr-date_inv).days/365.25
            dt=max(dt,0)
            age_retr2=max(age_retr,age)
            if anc_proj>mini:
                prov_lf[i][0]=min(max(mt_mini,min(droit(table,anc_proj),maxi))*salarie[i][3]/12,mt_maxi)*lx[age_retr2+1][1]/lx[age+1][1]*exp((age_retr2-age)*log(1+infl))
                prov_lf[i][0]=prov_lf[i][0]*exp(dt*log(1/(1+tech)))*exp(dt*log(1-to))*anc/anc_proj

            if anc_proj<=mini:
                prov_lf[i][0]=0
            duration[age_retr2-age][0]=duration[age_retr2-age][0]+prov_lf[i][0]
            dt2=int(dt)
            for j in range(0,dt2):
                facteur=(ly[age+j+1][1]-ly[age+j+2][1])/ly[age+1][1]*exp((j)*log(1+infl))
                somme=0
                for k in range(1,12):
                    anc2=anc+j+k/12
                    if anc2>mini:
                        somme=somme+1/12*exp((j+k/12)*log(1/(1+tech)))*min(max(mt_mini,min(droit(table,anc2),maxi))*salarie[i][3]/12,mt_maxi)*exp((anc2-anc)*log(1-to))*anc/anc2
                    if anc2<=mini:
                        somme=somme+0
                duration[j][1]=duration[j][1]+facteur*somme
                prov_dc[i][0]=prov_dc[i][0]+facteur*somme

            dt3=int((dt-dt2)*12)
            somme = 0
            facteur=(ly[age+j+1][1]-ly[age+j+2][1])/ly[age+1][1]*exp((dt2)*log(1+infl))
            for k in range(1,dt3+1):
                anc2=anc+dt2+k/12
                if anc2>mini:
                    somme=somme+1/12*exp((dt2+k/12)*log(1/(1+tech)))*min(min(droit(table,anc2),maxi)*salarie[i][3]/12,mt_maxi)*exp((anc2-anc)*log(1-to))*anc/anc2
                if anc2<=mini:
                    somme=somme+0
            duration[dt2][1]=duration[dt2][1]+facteur*somme
            prov_dc[i][0]=prov_dc[i][0]+facteur*somme
                        
    

    if prop==3:
        table=readlaw(loi)[7]
        print(table)
        tabler=retire(loi)
        print(tabler)
        fdeces=abondeces(loi)[0]
        print(fdeces)
        plfd=abondeces(loi)[1]
        print(plfd)
        for i in range(debut, fin):
            age=0
            age=annee_inv-salarie[i][1].year
            anc=(date_inv-salarie[i][2]).days/365.25
            depart_retr=datetime(salarie[i][1].year+age_retr, salarie[i][1].month, 1)
            anc_proj=max((depart_retr-salarie[i][2]).days/365.25,anc)
            dt=(depart_retr-date_inv).days/365.25
            dt=max(dt,0)
            age_retr2=max(age_retr,age)
            if anc_proj>mini:
                prov_lf[i][0]=min(max(mt_mini,min(droit(table,anc_proj),maxi))*salarie[i][3]/12,mt_maxi)*lx[age_retr2+1][1]/lx[age+1][1]*exp((age_retr2-age)*log(1+infl))
                prov_lf[i][0]=prov_lf[i][0]*exp(dt*log(1/(1+tech)))*exp(dt*log(1-to))*anc/anc_proj*droit2(tabler,age_retr2,anc_proj)

            if anc_proj<=mini:
                prov_lf[i][0]=0
            duration[age_retr2-age][0]=duration[age_retr2-age][0]+prov_lf[i][0]
            dt2=int(dt)
            for j in range(0,dt2):
                facteur=(ly[age+j+1][1]-ly[age+j+2][1])/ly[age+1][1]*exp((j)*log(1+infl))
                somme=0
                for k in range(1,12):
                    anc2=anc+j+k/12
                    if anc2>mini:
                        somme=somme+1/12*exp((j+k/12)*log(1/(1+tech)))*min(max(mt_mini,min(droit(table,anc2),maxi)+min(fdeces*anc2,plfd))*salarie[i][3]/12,mt_maxi)*exp((anc2-anc)*log(1-to))*anc/anc2
                    if anc2<=mini:
                        somme=somme+0
                duration[j][1]=duration[j][1]+facteur*somme
                prov_dc[i][0]=prov_dc[i][0]+facteur*somme

            dt3=int((dt-dt2)*12)
            somme = 0
            facteur=(ly[age+j+1][1]-ly[age+j+2][1])/ly[age+1][1]*exp((dt2)*log(1+infl))
            for k in range(1,dt3+1):
                anc2=anc+dt2+k/12
                if anc2>mini:
                    somme=somme+1/12*exp((dt2+k/12)*log(1/(1+tech)))*min(max(mt_mini,min(droit(table,anc2),maxi)+min(fdeces*anc2,plfd))*salarie[i][3]/12,mt_maxi)*exp((anc2-anc)*log(1-to))*anc/anc2
                if anc2<=mini:
                    somme=somme+0
            duration[dt2][1]=duration[dt2][1]+facteur*somme
            prov_dc[i][0]=prov_dc[i][0]+facteur*somme
                        
    for i in range(debut,fin):
        prov_vie=prov_vie+prov_lf[i][0]
        prov_deces=prov_deces+prov_dc[i][0]
        masse=masse+salarie[i][3]
    ratio=prov_vie/masse
    return(prov_vie,prov_deces,masse, nb_salarie, ratio, pyr, duration)


