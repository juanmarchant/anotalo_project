from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TaskManager(models.Manager):

    def task_validator(self, post_data):
        errors = {}
        
        if len(post_data['content']) == 0:
            errors['content'] = 'Should be at least content in the task'
            
        if len(post_data['content']) > 130:
            errors['content'] = 'You can only make task with 130 characters'
        return errors

class Task(models.Model):
    user = models.ForeignKey(User, related_name='tasks', on_delete= models.CASCADE)
    content = models.TextField(max_length=130)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    objects = TaskManager()

class TaskColor(models.Model):
    task = models.OneToOneField(Task, related_name='colors',on_delete=models.CASCADE)
    color = models.CharField(max_length=150, null=True)
    glue_color = models.CharField(max_length=150)
    content_color = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)