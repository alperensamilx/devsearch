from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'base/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)

    return render(request, 'base/single-project.html', {'project': projectObj})


def create_project(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'base/project_form.html', context)


def update_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'base/project_form.html', context)


def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    context = {'object': project}
    return render(request, 'base/delete_template.html', context)