#coding=utf-8
#!/usr/bin/python

from django import forms


class TaskForm(forms.Form):
    name = forms.CharField(max_length=100)
    source = forms.CharField(max_length=500)
    dist_path = forms.CharField(max_length=500)
    description = forms.CharField(max_length=5000)
