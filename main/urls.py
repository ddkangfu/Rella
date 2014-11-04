#coding=utf-8
#!/usr/bin/python

from django.conf.urls import patterns, include, url

from main.views import CreateTeskView, TaskListView, UpdateTaskView, DeleteTaskView

urlpatterns = patterns('',
    url(r'^list/$', TaskListView.as_view(), name='task_list'),
    url(r'^detail/(?P<pk>\d+)/$', 'main.views.task', name='detail_task'),
    url(r'^add/$', CreateTeskView.as_view(), name='task_add'),
    url(r'^edit/(?P<pk>\d+)/$', UpdateTaskView.as_view(), name='task_edit'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteTaskView.as_view(), name='task_delete'),
    url(r'^svn/(?P<task_id>\d+)/$', 'main.views.get_svn_info', name='get_svn_info'),
)