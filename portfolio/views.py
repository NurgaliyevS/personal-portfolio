from django.shortcuts import render
from .models import Project

## функция для домашней страницы
def home (request):
    ## DJANGO Импортирует все данные из базы данных
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})



# Create your views here.
