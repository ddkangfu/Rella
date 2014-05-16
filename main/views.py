#coding=utf-8
#!/usr/bin/python

from django.shortcuts import render_to_response


def index(request):
    return render_to_response('main/index.html')


def task_list(request):
    return render_to_response('main/task.html')


def task(rqeuest, task_id):
    return render_to_response('main/task.html')


def task_add(rqeuest):
    return render_to_response('main/task.html')


def task_edit(rqeuest, task_id):
    return render_to_response('main/task.html')


def task_delete(rqeuest, task_id):
    return render_to_response('main/task.html')

