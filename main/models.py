from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=100)
    svn_source = models.CharField(max_length=500)
    dist_path = models.CharField(max_length=500)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=5000, blank=True)
    is_enabled = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name
