#coding=utf-8
#!/usr/bin/python

from django.shortcuts import render_to_response


def login(request):  
    return render_to_response("accounts/login1.html")
 
'''
用户登出页
'''
def logout(request):  
    pass  