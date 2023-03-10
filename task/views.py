from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# função que adiciona tasks a lista.

def index(request):
    tasks = Task.objects.all()

    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
        
    context = {'tasks': tasks, 'form': form}
    return render(request, 'task/lista.html', context)

# função que permite atualizar o andamento da task.

def updateTask(request, pk):
    
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request, 'task/update_task.html', context)

# função que apaga a task

def delete(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect('/')

    context = {'task': task}

    return render(request, 'task/delete.html', context)