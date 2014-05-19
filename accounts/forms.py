#coding=utf-8
#!/usr/bin/python

from django import forms
from django.contrib.auth.forms import AuthenticationForm


class AuthUserForm(forms.Form):
    username = forms.CharField(max_length=254, error_messages={'required': u'请输入用户名'})
    password = forms.CharField(max_length=30, error_messages={'required': u'请输入密码'})    
    remberme = forms.BooleanField(required=False)
