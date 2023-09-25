from django.http import HttpResponse # Importamos la clase HttpResponse de Django
from django.template import Template, Context, loader # Importamos la clase Template y Context de Django

# def mi_vista(request):
#     html = "<html><body><h1>Mi Página Web</h1></body></html>"
#     return HttpResponse(html)

def saludo(request):
	return HttpResponse("Hola Django - Coder")

def segunda_vista(request):
	return HttpResponse("<h2>Segunda vista</h2>")

def miNombreEs(self, nombre):
	data = f"Mi nombre es: <h2>{nombre}</h2>"
	return HttpResponse(data)


""" template con variables utilizando context y template"""

""" def probandoTemplate(self):
	nombre = "Johanna"
	apellido = "Tumio"

	namelist = ["Gabriel", "Ana", "Lisa", "Patricia", "Pedro"]

	diccionario = {
		"nombre":nombre,
		"apellido":apellido,
		"listaNombre": namelist 
	}

	#with open("C:/Users/BANGHO/Desktop/django/Proyecto1/Proyecto1/plantillas/template1.html", "r") as miHtml:
	miHtml = open("C:/Users/BANGHO/Desktop/django/Proyecto1/Proyecto1/plantillas/template1.html") 
	plantilla = Template(miHtml.read()) 
	miHtml.close() 
	miContext = Context(diccionario) #recibe el diccionario q tiene la informacion
	documento = plantilla.render(miContext)
	return HttpResponse(documento) """


""" Template utilizando loader """

""" Dentro del contexto de las plantillas, los "loaders" son responsables de buscar y cargar las plantillas desde diferentes fuentes, como sistemas de archivos locales, bases de datos o cualquier otro lugar donde puedan estar almacenadas las plantillas.  """

def probandoTemplate(self):
	nombre = "Johanna"
	apellido = "Tumio"

	namelist = ["Gabriel", "Ana", "Lisa", "Patricia", "Pedro"]

	diccionario = {
		"nombre":nombre,
		"apellido":apellido,
		"listaNombre": namelist 
	}
	#se utiliza el objeto loader para cargar la plantilla llamada "template1.html"
	plantilla = loader.get_template("template1.html") #se pone loader.get_template("nombreDeLaTemplate")
	documento = plantilla.render(diccionario) # se renderiza la plantilla utilizando los datos proporcionados en el diccionario. Esto significa que cualquier variable dentro de la plantilla que esté definida en el diccionario (como "nombre", "apellido" y "listaNombre") se reemplazará con los valores correspondientes.
	return HttpResponse(documento)

#En resumen, este código carga una plantilla HTML utilizando el objeto loader de Django, pasa un diccionario de datos a la plantilla y luego devuelve el HTML renderizado como una respuesta HTTP. 



""" guardando datos en base de datos y mostrarlos en una pagina """
""" aqui estamos creando una funcion de vista para q se vea x la pag """

from AppCoder.models import Curso #importamos al modelo curso q esta en la AppCoder en el archivo models

def curso(self):
	curso = Curso(nombre = "javascript", camada = 15248) #instanciamos al modelo curso
	curso.save() #lo guardamos en la base de datos
	docTexto = f"--->Curso: {curso.nombre} Camada: {curso.camada}" #lo q queremos q salga en la pag

	return HttpResponse(docTexto)


""" crear varias instancias de curso a la vez """
def cursos(request):
    # Crear varias instancias de Curso y guardarlas en una lista
    cursos = [
        Curso(nombre="react Js", camada=15248),
        Curso(nombre="desarrollo web", camada=15269),
        # Agrega más instancias de Curso según sea necesario
    ]
    
    # Guardar todas las instancias en la base de datos
    Curso.objects.bulk_create(cursos)
    
    # Recuperar todos los cursos de la base de datos
    cursos = Curso.objects.all()
    
    # Mensaje de éxito
    docTexto = "Se han creado y recuperado varios cursos:<br>"
    
    # Iterar sobre los cursos y mostrar sus datos
    for curso in cursos:
        docTexto += f"Curso: {curso.nombre} Camada: {curso.camada}<br>"
    
    return HttpResponse(docTexto, content_type='text/html')




""" template sin variables """
""" def probandoTemplate(self):
	# Paso 1: Abrir y leer el archivo de la plantilla HTML.
	miHtml = open("C:/Users/BANGHO/Desktop/django/Proyecto1/Proyecto1/plantillas/template1.html") 
	plantilla = Template(miHtml.read()) # Creamos una instancia de Template a partir del contenido del archivo y se lee con read().
	miHtml.close() # Cerramos el archivo después de leerlo.

	# Paso 2: Crear un contexto vacío. 
	miContext = Context() # Creamos un objeto Context vacío. en este caso va vacio xq le asignamos un html. El uso de un contexto vacío es adecuado para plantillas que son estáticas y no requieren datos dinámicos. 

	# Paso 3: Renderizar la plantilla con el contexto.
	documento = plantilla.render(miContext) #de plantilla renderizamos(pintamos) miContex. (renderizamos plantilla q es el template q creamos)

	# Paso 4: Devolver una respuesta HTTP con el contenido de la plantilla.
	return HttpResponse(documento) # Devolvemos una respuesta HTTP que contiene el contenido renderizado. """




""" otro ej de probando template """
""" def probandoTemplate(request):
    # Paso 1: Abrir y leer el archivo de la plantilla HTML.
    with open("C:/Users/BANGHO/Desktop/django/Proyecto1/Proyecto1/plantillas/template1.html") as miHtml:
        template = Template(miHtml.read())

    # Paso 2: Crea un contexto para la plantilla (puedes agregar datos al contexto si es necesario).
    miContext = Context({
        'nombre': 'Juan',  # Ejemplo de dato que puedes pasar a la plantilla.
    })

    # Paso 3: Renderiza la plantilla con el contexto.
    documento = template.render(miContext)

    # Paso 4: Devuelve una respuesta HTTP con el contenido de la plantilla.
    return HttpResponse(documento) """

