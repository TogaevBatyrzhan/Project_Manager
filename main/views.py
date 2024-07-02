from functools import wraps
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from projects.models import Project
from tasks.models import Task 

def check_project_permission(view_func):
    @wraps(view_func)
    def _wrapped_view(request, project_id, *args, **kwargs):
        project = get_object_or_404(Project, id=project_id)
        if project.owner != request.user:
            messages.error(request, "Вы не имеете права редактировать этот проект.")
            return redirect('project_detail', project_id=project_id)
        return view_func(request, project_id, *args, **kwargs)
    return _wrapped_view

def check_task_permission(view_func):
    @wraps(view_func)
    def _wrapped_view(request, project_id, task_id, *args, **kwargs):
        project = get_object_or_404(Project, id=project_id)
        task = get_object_or_404(Task, id=task_id, project=project)
        if task.assigned_to != request.user and project.owner != request.user:
            messages.error(request, "Вы не имеете права редактировать эту задачу.")
            return redirect('task_detail', project_id=project_id, task_id=task_id)
        return view_func(request, project_id, task_id, *args, **kwargs)
    return _wrapped_view