"""isr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from calculer import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('isr/', login_required(views.home), name='home'),
    path('date/',login_required(views.entree), name='entree'),
    path('age_retraite/',login_required(views.entree2), name='entree2'),
    path('employes/',login_required(views.entree3), name='entree3'),
    path('loi/',login_required(views.entree4), name='entree4'),
    path('tech/', login_required(views.entree5), name='entree5'),
    path('turnover/', login_required(views.entree6), name='entree6'),
    path('Result/', login_required(views.sortie), name='sortie'),
]
