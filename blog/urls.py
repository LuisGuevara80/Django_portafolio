from django.urls import path
from .views import render_post, post_detail

app_name = 'blog' # Define un espacio de nombres para las URLs de la aplicación 'blog', evitando conflictos de nombres y facilitando su referencia en otras partes del proyecto.

urlpatterns = [
    path('', render_post, name='posts'),
    path('post/<int:post_id>', post_detail, name='post_detail'), # En este se espera como parametro el id del post que queremos mostrar
]

