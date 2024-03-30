from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Message
from .forms import MessageForm


def index(request):
    return render(request, 'message.html')


def my_view(request):
    users = Message.objects.all()
    return render(request, 'chat.html', {'users': users})


class MyDetailView(DetailView):
    model = Message
    template_name = 'detail.html'
    context_object_name = 'message'


def create(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entering')
    else:
        form = MessageForm()
    return render(request, 'entering_messages.html', {'form': form})
