from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField


class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=500)
    image = ImageField(upload_to='portafolio/images')     
    url = URLField(blank=True) # Esto da la opción de que se pueda colocar una URL o no.
