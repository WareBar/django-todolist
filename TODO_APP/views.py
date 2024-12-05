from django.shortcuts import render, redirect
from TASK.models import Tasks
from TASK.forms import Task

def Todo(request):
    
    tasks = Tasks.objects.all()
    if request.method == 'POST':
        form = Task(request.POST)
        if form.is_valid():
            form.save()
            return redirect('HOME')
    else:
        form = Task()


    return render(request, 'todo_page.html',{
        'tasks':tasks,
        'checked': len(Tasks.objects.filter(completed=True)),
        'total':len(tasks),
        'addTaskForm':Task
    })