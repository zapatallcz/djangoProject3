from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task


# Create your views here.

def index_task(request):
    tasks = Task.objects.all()
    form = TaskForm(request.POST)
    context = {'tasks': tasks, 'form': form}
    return render(request, 'todo/index.html', context)


def add_task(request):
    form = TaskForm(request.POST or None)
    # check whether it's valid:
    if form.is_valid():
        # save the record into the db
        form.save()
        # after saving redirect to view_product page
        return redirect('index_task')
    return render(request, 'todo/index.html')


def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    # populate a form instance with data from the data on the database
    # instance=product allows to update the record rather than creating a new record when save method is called
    form = TaskForm(request.POST or None, instance=task)

    # check whether it's valid:
    if form.is_valid():
        # update the record in the db
        form.save()
        # after updating redirect to view_product page
        return redirect('index_task')

    # if the request does not have post data, render the page with the form containing the product's info

    context = {'form': form, 'task': task}
    return render(request, 'todo/update.html', context)


def delete_task(request, task_id):
    # Get the product based on its id
    task = Task.objects.get(id=task_id)

    # if this is a POST request, we need to delete the form data
    if request.method == 'POST':
        task.delete()
        # after deleting redirect to view_product page
        return redirect('index_task')

    # if the request is not post, render the page with the product's info
    context = {'task': task}
    return render(request, 'todo/delete.html', context)


def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('index_task')


