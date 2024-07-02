from django.urls import path
from . import views

urlpatterns = [
    path('Catalog/', views.Catalog, name="Catalog")
]