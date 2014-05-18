#coding=utf-8
#!/usr/bin/python

from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib import auth


def login(request):  
	err_msg = ''
	
	if request.method == 'POST':
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		next_url = request.POST.get('next', '')
		is_remberme = request.POST.get('remberme', False)
		user = auth.authenticate(username=username, password=password)
		if user is not None and user.is_active:
			auth.login(request, user)
			if next_url:
				return HttpResponseRedirect(next_url)
			return HttpResponseRedirect("/")
		else:
			return HttpResponseRedirect("/account/invalid/")
	return render_to_response("accounts/login.html", {"err_msg": err_msg})
 
'''
用户登出页
'''
def logout(request):  
    pass  