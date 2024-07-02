from django.urls import path
from . import views

urlpatterns = [
    path('projects/<int:project_id>/tasks/<int:task_id>/', views.details_task, name='details_task'),
    path('projects/<int:project_id>/tasks/create/', views.create_task, name='create_task'),
    path('projects/<int:project_id>/tasks/<int:task_id>/edit/', views.edit_task, name='edit_task'),
    path('projects/<int:project_id>/tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('projects/<int:project_id>/tasks/<int:task_id>/change_status/', views.change_task_status, name='change_task_status'),
]
