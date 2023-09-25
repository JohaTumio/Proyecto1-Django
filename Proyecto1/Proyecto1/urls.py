"""
URL configuration for Proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Proyecto1.views import saludo, segunda_vista, miNombreEs, probandoTemplate, curso, cursos #Para acceder a la vista hay que importar el modulo y el método
from AppCoder.views import cursoAppCoder, estudiantes


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludos/', saludo), #ojo la url no hace falta que se llame saludo/ el nombre es libre, pero la vista sí debe llamarse por su nombre(a q funcion obedece)
    path('segundavista/', segunda_vista),
    path('miNombreEs/<nombre>', miNombreEs), #recibe un parametro mas en la url http://127.0.0.1:8000/miNombreEs/Joha
    path('probandoTemplate/', probandoTemplate),
    path('curso/', curso),
    path('cursos/', cursos),
    path('cursoAppCoder/', cursoAppCoder),
    path('Listaestudiantes/', estudiantes),

]
