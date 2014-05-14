from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=100)
    source = models.CharField(max_length=500)
    dist_path = models.CharField(max_length=500)
    create_time = models.DateTimeField( auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=5000)

    def __unicode__(self):
        return self.name
