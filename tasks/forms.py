from django.db.models import fields
from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'status']

class CreateTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title']