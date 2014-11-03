#coding=utf-8
#!/usr/bin/python

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^list/$', 'main.views.task_list', name='task_list'),
    url(r'^(?P<task_id>\d+)/$', 'main.views.task', name='task'),
    url(r'^add/$', 'main.views.task_add', name='task_add'),
    url(r'^edit/(?P<task_id>\d+)/$', 'main.views.task_edit', name='task_edit'),
    url(r'^delete/(?P<task_id>\d+)/$', 'main.views.task_delete', name='task_delete'),
    url(r'^svn/(?P<task_id>\d+)/$', 'main.views.get_svn_info', name='get_svn_info'),
)