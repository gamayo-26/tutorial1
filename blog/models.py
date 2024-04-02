from django.db import models

""" archivo que se utiliza para crear tablas en la base de datos. 
Esto se hace creando clases que heredan de models.Model y 
definiendo los atributos dentro de esta. Cada atributo representa una columna
en la tabla de la base de datos.

Cada vez que se modifica este archivo, se debe correr el comando 
'python manage.py makemigrations' para que Django actualice la 
base de datos con los cambios."""

# Create your models here.
class Post(models.Model):
    # creamos un campo el la base de datos de tipo texto
    title=models.CharField(max_length=250)
    #el textfield es un campo de texto mas largo que el charfield
    content=models.TextField()

    '''Podemos modificar como se muestra el objeto en el panel del 
    administrador de Django sobreescribiendo el metodo __str__'''
    def __str__(self):
        return self.title