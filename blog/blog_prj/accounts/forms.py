from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from users.models import User

class SignUpForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'nickname']