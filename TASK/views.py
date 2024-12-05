from django.shortcuts import render, redirect
from TASK.models import Tasks

# Create your views here.


def completeTask(request, task_id, action):
    task = Tasks.objects.get(id=task_id)
    if action == 'CHECK':
        task.completed = True
    elif action == 'UNCHECK':
        task.completed = False
    task.save()
    return redirect('HOME')


def deleteTask(request, task_id):
    task = Tasks.objects.get(id=task_id)
    task.delete()
    return redirect('HOME')