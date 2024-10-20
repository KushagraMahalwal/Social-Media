from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class createPost(models.Model):
    text=models.TextField()
    created_by=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return self.created_by



