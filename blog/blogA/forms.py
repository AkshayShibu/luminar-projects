from django.forms import ModelForm
from django import forms
from blogA.models import Content

class Content_Form(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'describtion']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'describtion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter description'}),
        }