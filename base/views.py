from django.shortcuts import render
from .models import *

# Create your views here.


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'base/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)

    return render(request, 'base/single-project.html', {'project': projectObj})

