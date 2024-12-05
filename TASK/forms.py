from django import forms
from . import models

class Task(forms.ModelForm):
    class Meta:
        model = models.Tasks
        fields = ['todo',]