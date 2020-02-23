from django import forms

from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['email', 'msg_text']

    widgets = {
        'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        'msg_text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message text'})
    }
