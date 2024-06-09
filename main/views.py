from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Message
from .forms import MessageForm, RegisterForm


def main(request):
    return render(request, 'message.html')


def my_view(request):
    users = Message.objects.all()
    return render(request, 'chat.html', {'users': users[::-1]})




@login_required
def create(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chat')
    else:
        form = MessageForm()
    return render(request, 'entering_messages.html', {'form': form})



def registr(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            users = form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/registr.html', {'form': form})