#coding=utf-8
#!/usr/bin/python

from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['create_time', 'update_time']
