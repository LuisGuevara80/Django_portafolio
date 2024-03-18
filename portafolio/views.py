from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all() # Consulo a todos los proyectos que tengo en mi base de datos.
    return render(request, 'home.html', {
        'projects' : projects
    }) # render ya conoce que existe una carpeta templates donde van a estar las páginas hmtl.
