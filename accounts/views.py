#coding=utf-8
#!/usr/bin/python

from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import auth

from forms import AuthUserForm


def login(request):  
	err_msg = ''
	next_url = request.REQUEST.get('next', '')
	datas = {'err_msg': '',
			 'next': next_url,
			}
	if request.method == 'POST':
		form = AuthUserForm(request.POST)
		if not form.is_valid():
			err_msg = ','.join([err.as_text().split(' ')[1].strip()
                            for err in form.errors.values()])
			datas['err_msg'] = err_msg
			return render(request, "accounts/login.html", datas)

		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		is_remberme = form.cleaned_data.get('remberme')

		user = auth.authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth.login(request, user)
				if next_url:
					return HttpResponseRedirect(next_url)
				return HttpResponseRedirect(reverse("index"))
			else:
				err_msg = "用户未被启用。"
		else:
			err_msg = "用户名或密码错误。"

	datas['err_msg'] = err_msg
	return render(request, "accounts/login.html", datas)

'''
用户登出页
'''
def logout(request):  
    auth.logout(request)
    return HttpResponseRedirect(reverse("login"))


def setting(request):
	return render(request, "accounts/setting.html", None)