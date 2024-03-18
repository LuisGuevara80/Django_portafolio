from django.db import models
from django.db.models.fields import CharField, URLField, TextField, DateField
from django.db.models.fields.files import ImageField
import datetime

class Post(models.Model):
    title = CharField(max_length=100)
    description = TextField()
    image = ImageField(upload_to='blog/images')
    date = DateField(datetime.date.today) # Si no se proporciona una fecha, se utiliza la fecha actual.

