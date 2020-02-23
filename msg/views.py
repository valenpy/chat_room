from django.shortcuts import render, redirect

from .forms import MessageForm
from .models import Message


def index(request):
    messages = Message.objects.all()
    return render(request, 'index.html', {
        'messages': messages
    })


def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            new_post = form.save()
            new_post.save()
            return redirect('chat')

    else:
        form = MessageForm()

    return render(request, 'index.html', {
        'form': form
    })
