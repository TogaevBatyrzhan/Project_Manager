from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Position


User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    position = forms.ModelChoiceField(queryset=Position.objects.all(), required=True, label="Выберите должность")

    class Meta:
        model = User
        fields = ('username', 'email','first_name', 'password1', 'password2', 'position')
