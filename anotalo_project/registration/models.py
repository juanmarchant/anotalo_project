from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profiles/avatar', null=True, blank="True")
    background = models.ImageField(upload_to='profiles/background', null=True, blank="True")
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)