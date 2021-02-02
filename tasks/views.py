from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

@login_required(login_url='/')
def index(request):
    current_user = request.user
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        
        if form.is_valid():
            count = Task.objects.filter(user_id=current_user.id).count()
            task = form.save(commit=False)
            task.user_id = current_user.id
            task.order = count + 1
            task.save()
        return redirect('list')
    
    form = CreateTaskForm()
    tasks = Task.objects.filter(user_id=current_user.id).order_by('order')

    context = {'tasks': tasks, 'form': form}
    return render(request,'tasks/list.html', context)

@login_required(login_url='/')
def updateTask(request, pk):
    current_user = request.user
    task = Task.objects.get(id=pk, user_id=current_user.id)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/list')

    context = {'form':form}

    return render(request, 'tasks/update.html', context)

@login_required(login_url='/')
def deleteTask(request, pk):
    current_user = request.user
    item = Task.objects.get(id=pk, user_id=current_user.id)

    if request.method == 'POST':
        item.delete()
        return redirect('/list')

    context = {'item':item}
    return render(request, 'tasks/delete.html', context)

def moveTaskUp(request, pk):
    current_user = request.user
    task = Task.objects.get(id=pk, user_id=current_user.id)
     
    previousTask = Task.objects.filter(user_id=current_user.id, order=task.order-1).first()
    if previousTask is not None:
        previousTask.order = previousTask.order+1
        task.order = task.order-1
        previousTask.save()
        task.save()
    return redirect('/list')


def moveTaskDown(request, pk):
    current_user = request.user
    task = Task.objects.get(id=pk, user_id=current_user.id)
     
    previousTask = Task.objects.filter(user_id=current_user.id, order=task.order+1).first()
    if previousTask is not None:
        previousTask.order = previousTask.order-1
        task.order = task.order+1
        previousTask.save()
        task.save()
    return redirect('/list')