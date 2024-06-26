from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class RegisterForm(UserCreationForm):


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')