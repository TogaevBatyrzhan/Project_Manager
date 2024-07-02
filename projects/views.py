from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
from tasks.models import Task
from main.views import check_project_permission


@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.project_manager = request.user
            project.save()
            return redirect('list_projects')
    else:
        form = ProjectForm()
    return render(request, 'create_project.html', {'form': form})

@login_required
@check_project_permission
def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.user != project.project_manager:
        return redirect('list_projects')
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('details_project', project_id=project.id)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'edit_project.html', {'form': form, 'project': project})

def list_projects(request):
    if request.user.is_authenticated:
        projects = Project.objects.filter(project_manager=request.user)
        return render(request, 'list_projects.html', {'projects': projects})
    else:
        return redirect('login')  # Перенаправление на страницу входа


def details_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    tasks_new = Task.objects.filter(project=project, status='new')
    tasks_in_progress = Task.objects.filter(project=project, status='in_progress')
    tasks_on_verification = Task.objects.filter(project=project, status='on_verification')
    tasks_completed = Task.objects.filter(project=project, status='completed')
    
    context = {
        'project': project,
        'tasks_new': tasks_new,
        'tasks_in_progress': tasks_in_progress,
        'tasks_on_verification': tasks_on_verification,
        'tasks_completed': tasks_completed,
    }
    
    return render(request, 'project_detail.html', context)