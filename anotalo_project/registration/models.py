from django.db import models
from django.contrib.auth.models import User

def custom_upload_to_avatar(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    
    return 'profiles/avatar' + filename

def custom_upload_to_background(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.background.delete()
    
    return 'profiles/background' + filename


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to_avatar, null=True, blank="True")
    background = models.ImageField(upload_to=custom_upload_to_background, null=True, blank="True")
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)