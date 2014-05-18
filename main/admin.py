#coding=utf-8
#!/usr/bin/python

from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    fields  = ['name', 'svn_source', 'dist_path', 'description', 'is_enabled', 'latest_runing_time']
    list_display = ('name', 'svn_source', 'description', 'create_time', 'update_time', 'latest_runing_time', 'is_enabled')


admin.site.register(Task, TaskAdmin)
