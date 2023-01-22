from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete,pre_save

# Create your models here.


class Events(models.Model):
    events_name = models.CharField(max_length=100,blank=True,null=True)
    meeting_date_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.events_name)