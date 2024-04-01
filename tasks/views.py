from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# task_view - Input is request
def task_view(request):
    # is request equals POST
    if request.method == "POST":
        # get the form post data
        form = TaskForm(request.POST)
        # if form is valid
        if form.is_valid():
            # save form data
            form.save()
            # redirect to task view showing updates
            return redirect('pages/task_view')
    else:
        form = TaskForm() # An unbound form for GET requests
    # get active task filter
    active_tasks = Task.objects.filter(completed=False)
    # get completed task filter
    completed_tasks = Task.objects.filter(completed=True)
    # return task_view passing in form / active_tasks / completed_tasks
    return render(request, 'pages/task_view.html', {
        'form': form,
        'active_tasks': active_tasks,
        'completed_tasks': completed_tasks,
    })

# Add_Task - Input Request
def add_task(request):
    # if request equals POST
    if request.method == "POST":
        # Get form post data
        form = TaskForm(request.POST)
        # if form is valid
        if form.is_valid():
            # save form data
            form.save()
            # redirect to task_view
            return redirect('task_view')  # Redirect to the task list after saving
    else:
        form = TaskForm()  # An unbound form for GET requests
    # return add_task html
    return render(request, 'pages/add_task.html', {'form': form})

# toggle_task input is request and task_id
def toggle_task(request, task_id):
    # get the task or get 404 if nothing
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed  # Toggle the task's status
    task.save() # save task
    return redirect('task_view')  # Redirect back to the task view page

