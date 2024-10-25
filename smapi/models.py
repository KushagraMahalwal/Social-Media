from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class createPost(models.Model):
    text=models.TextField()
    created_by=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name="crateposts")
    liked_by=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name="like", blank=True)

    def __str__(self):
        return f"created_by{self.created_by}"

class comment(models.Model):
    comm=models.TextField(max_length=100)
    post=models.ForeignKey(createPost, on_delete=models.CASCADE, related_name="comments")
    commented_by=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="commentt")

    def __str__(self):
        return f"Comment by {self.commented_by.username}"  # Optional for better readability





