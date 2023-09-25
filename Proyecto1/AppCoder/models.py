""" En Django, los modelos son una parte fundamental de la creación y gestión de la base de datos de tu aplicación. Los modelos definen la estructura de las tablas en la base de datos y proporcionan una capa de abstracción para interactuar con la base de datos utilizando objetos Python en lugar de escribir consultas SQL directamente.  """

""" models.Model es una clase base proporcionada por Django que contiene toda la funcionalidad necesaria para que tu clase se comunique con la base de datos de forma efectiva.
Django utiliza la información en tu clase que hereda de models.Model para crear automáticamente una tabla en la base de datos con el mismo nombre que el nombre de la clase en minúsculas. Por ejemplo, si tienes una clase llamada Curso, Django creará una tabla llamada curso en la base de datos. """

""" Dentro de cada modelo, has definido una serie de campos que representan las columnas de la tabla en la base de datos. Los atributos definidos en tu clase, como CharField, IntegerField, DateField, etc., se utilizan para especificar qué columnas debe tener la tabla en la base de datos y cómo se deben almacenar los datos en esas columnas. 

models.CharField(max_length=30): Este campo se utiliza para almacenar cadenas de texto con una longitud máxima de 30 caracteres. Se utiliza para almacenar nombres, apellidos y otros datos de texto corto.

models.EmailField(): Este campo se utiliza específicamente para almacenar direcciones de correo electrónico. Asegura que los datos ingresados sean direcciones de correo electrónico válidas.

models.IntegerField(): Este campo se utiliza para almacenar números enteros.

models.DateField(): Este campo se utiliza para almacenar fechas.

models.BooleanField(): Este campo se utiliza para almacenar valores booleanos (verdadero o falso).
"""

from django.db import models

# Create your models here.

class Curso(models.Model): #estás diciendo que esta clase será un modelo que Django debe administrar en la base de datos.
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()
    entregada = models.BooleanField()
