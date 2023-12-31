from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('task_list')
    return render(request, 'tasks/add_task.html')

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.title = request.POST.get('title')
        task.save()
        return redirect('task_list')
    return render(request, 'tasks/edit_task.html', {'task': task})

#pk is primary key, could be id
def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = True
    task.save()
    return redirect('task_list')

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')