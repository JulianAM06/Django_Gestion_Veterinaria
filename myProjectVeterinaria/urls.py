"""
URL configuration for myProjectVeterinaria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from myAppGestion.views import index, registrarMascota, mostrarMascota, registrarCliente, mostrarCliente,registrarTratamiento, mostrarTratamiento, registarAdopciones, mostrarAdopcion, salir
from myAppDescargar.views import archivo, descargar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('registrarMascota/', registrarMascota, name='registrarMascota'),
    path('registrarMascota/mostrarMascota/', mostrarMascota, name='mostrarMascota'),
    path('registrarCliente/', registrarCliente, name='registrarCliente'),
    path('registrarCliente/mostrarCliente/', mostrarCliente, name='mostrarCliente'),
    path('registrarTratamiento/', registrarTratamiento, name='registrarTratamiento'),
    path('registrarTratamiento/mostrarTratamiento/', mostrarTratamiento, name='mostrarTratamiento'),
    path('registrarAdopcion/', registarAdopciones, name='registrarAdopcion'),
    path('mostrarAdopcion/', mostrarAdopcion, name='mostrarAdopcion'),
    path('accounts/', include ('django.contrib.auth.urls')),
    path('logout/', salir, name='salir'),
    path('archivo/', archivo, name= 'archivo'),
    path('descargar/', descargar, name='descargar')
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)