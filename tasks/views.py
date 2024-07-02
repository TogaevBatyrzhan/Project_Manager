from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from projects.models import Project
from django.contrib.auth.decorators import login_required


@login_required
def create_task(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.creator = request.user
            task.save()
            return redirect('details_project', project_id=project.id)
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form, 'project': project})



def details_task(request, project_id, task_id):
    project = get_object_or_404(Project, id=project_id)
    task = get_object_or_404(Task, id=task_id)
    context = {
        'project': project,
        'task': task,
    }
    return render(request, 'details_task.html', context)


def edit_task(request, project_id, task_id):
    task = get_object_or_404(Task, id=task_id, project_id=project_id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('details_project', project_id=project_id)
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'edit_task.html', {'form': form, 'task': task})


def change_task_status(request, project_id, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        if task.status == 'new':
            task.status = 'in_progress'
        elif task.status == 'in_progress':
            task.status = 'on_verification'
        elif task.status == 'on_verification':
            task.status = 'completed'
        task.save()
        return redirect('details_project', project_id=project_id, task_id=task_id)

    return redirect('details_project', project_id=project_id, task_id=task_id)


def delete_task(request, project_id, task_id):
    task = get_object_or_404(Task, id=task_id, project_id=project_id)
    task.delete()
    return redirect('details_project', project_id=project_id)
