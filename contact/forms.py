from django.forms import ModelForm
from .models import Contact
from django import forms

class MyCommentForm(forms.ModelForm):
    class Meta(object):
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(
    attrs={
     'class': 'form-control'
     }
    ),
   'email': forms.TextInput(
    attrs={
     'class': 'form-control'
     }
    ),
   'subject': forms.TextInput(
    attrs={
     'class': 'form-control'
     }
    ),
            'message': forms.Textarea(
    attrs={
     'class': 'form-control'
     }
    ),
   }
