#coding=utf-8
#!/usr/bin/python

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^login/$', 'accounts.views.login',name="login"),
    url(r'^logout/$', 'accounts.views.logout',name="logout"),
    url(r'^setting/$', 'accounts.views.setting',name="satting"), 
)