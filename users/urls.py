from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome_page, name="welcome"),
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('profile/', views.profile_page, name='profile'),
    path('profile/edit/', views.edit_profile_page, name='edit_profile'),
    path('logout/', views.logout_view, name='logout'),
]