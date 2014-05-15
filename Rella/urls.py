from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'main.views.index', name='index'),
    url(r'^task/list/$', 'main.views.task_list', name='task_list'),
    url(r'^task/(?P<task_id>\d+)/$', 'main.views.task', name='task'),
    url(r'^task/add/$', 'main.views.task_add', name='task_add'),
    url(r'^task/edit/(?P<task_id>\d+)/$', 'main.views.task_edit', name='task_edit'),
    url(r'^task/delete/(?P<task_id>\d+)/$', 'main.views.task_delete', name='task_delete'),
    url(r'^accounts/index$', 'accounts.views.index',name="accounts_index"),  
	url(r'^accounts/register$', 'accounts.views.register',name="register"),  
	url(r'^accounts/login$', 'accounts.views.login',name="login"),  
	url(r'^accounts/logout$', 'accounts.views.logout',name="logout"),  
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
