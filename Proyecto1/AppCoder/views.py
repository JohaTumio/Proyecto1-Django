from django.shortcuts import render
from AppCoder.models import Curso, Estudiante #importamos al modelo curso q esta en la AppCoder en el archivo models
from django.http import HttpResponse #Importamos la clase HttpResponse de Django
from django.template import loader
#Dentro del contexto de las plantillas, los "loaders" son responsables de buscar y cargar las plantillas desde diferentes fuentes



# Create your views here.

def cursoAppCoder(self):
	curso1 = Curso(nombre = "javascript", camada = 15248) #instanciamos al modelo curso
	curso2 = Curso(nombre="react Js", camada=15248)
	curso1.save() #guardamos los datos en DB
	curso2.save()
	
	diccionario = {
		"curso1":curso1, #"curso1" puede tener otro nombre
		"curso2":curso2
    } #creamos diccionario para poder utilizar los datos en html
	
	plantilla = loader.get_template("cursos/listaCursos.html")
	documento = plantilla.render(diccionario)
	return HttpResponse(documento)


def estudiantes(self):
	estudiante1 = Estudiante(nombre = "Alexis", apellido = "Lopez", email = "alexis@gmail.com")
	estudiante2 = Estudiante(nombre = "Juan", apellido = "Romero", email = "juRomero@gmail.com")
	estudiante1.save()
	estudiante2.save()

	diccionario = {
		"estu1":estudiante1,
		"estu2":estudiante2
	}

	plantilla = loader.get_template("estudiantes/listaEstudiantes.html")
	documento = plantilla.render(diccionario)
	return HttpResponse(documento)
