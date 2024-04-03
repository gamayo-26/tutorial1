from django.contrib import admin


from .models import Post

""" archivo que se utiliza para que las tablas creadas en el models.py
se muestren en el panel de administracion de Django."""

# Register your models here.
admin.site.register(Post)