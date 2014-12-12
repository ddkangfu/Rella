#coding=utf-8
#!/usr/bin/python

#import pysvn
import json
import time

from django.shortcuts import render_to_response, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import (ListView, DetailView, CreateView,
                                  TemplateView, UpdateView, RedirectView,
                                  FormView, DeleteView)
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db import transaction
from django.utils.decorators import method_decorator

from .models import Task
from .forms import TaskForm


@login_required
def index(request):
    task_list = Task.objects.all()
    return render(request, 'main/index.html',  {'task_list': task_list})


class TaskListView(ListView):
    template_name = 'main/task/list.html'
    model = Task

    def get_queryset(self):
        queryset = Task.objects.filter(owner=self.request.user)
        return queryset


class DetailTaskView(DetailView):
    template_name = 'main/task.html'
    model = Task


class CreateTaskView(CreateView):
    template_name = 'main/task_form.html'
    model = Task
    form_class = TaskForm

    #@method_decorator(login_required)
    #def post(self, request, *args, **kwargs):
    #    pass

    #@method_decorator(transaction.atomic)
    #def form_valid(self, form):
    #    pass

    def get_context_data(self, **kwargs):
        ctx = super(CreateTaskView, self).get_context_data(**kwargs)
        return ctx

    #def get_item(self):
    #    pass

    #def get_success_url(self):
    #    return reverse('')


class UpdateTaskView(UpdateView):
    template_name = 'main/task/update.html'
    model = Task

    def get_success_url(self):
        return reverse('main:task_list')


class DeleteTaskView(DeleteView):
    template_name = 'main/task.html'
    model = Task


def get_svn_info(request, task_id):
    """
    task = get_object_or_404(Task, pk=task_id)
    client = pysvn.Client()
    log_list = client.log(task.svn_source, limit=1)
    result = {}
    if log_list:
        log = log_list[0]
        result['author'] = log["author"]
        result['revision'] = log['revision'].number
        result['date'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(log['date']))
        result['message'] = log['message']
    return HttpResponse(json.dumps(result,
                                   ensure_ascii=False,
                                   encoding="utf-8"),
                        content_type='application/json;charset=utf-8',
                        status=200)
    """
    pass


