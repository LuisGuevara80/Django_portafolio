from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name= 'home'), # El name nos sirve para poder navegar de manera más sencilla en esa url.
]
