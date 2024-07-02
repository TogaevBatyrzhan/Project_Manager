from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.list_projects, name='list_projects'),
    path('projects/<int:project_id>/', views.details_project, name='details_project'),
    path('create_project/', views.create_project, name='create_project'),
    path('projects/<int:project_id>/edit/', views.edit_project, name='edit_project'),
]