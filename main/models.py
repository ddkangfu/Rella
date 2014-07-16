#coding=utf-8
#!/usr/bin/python

from django.db import models


class Task(models.Model):
    """
    用来定义所有的发布任务
    """
    name = models.CharField(max_length=100)
    svn_source = models.CharField(max_length=500)
    dist_path = models.CharField(max_length=500)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    latest_runing_time = models.DateTimeField()
    description = models.CharField(max_length=5000, blank=True)
    is_enabled = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class Project(models.Model):
    """
    项目，用来定义所有项目信息
    """
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=5000, blank=True)
    svn_path = models.CharField(max_length=500)
    version = models.CharField(max_length=20)
    public_time = models.DateTimeField()
    build_file_name = models.CharField(max_length=200)
    release_note_file_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

#权限分为两级，管理员和操作员，管理员管理项目信息、分配项目权限，操作员只是进行一般的操作

