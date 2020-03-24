from django.db import models
from ..login.models import User

class Message(models.Model):
    message=models.TextField()
    #user
    #comments
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Comment(models.Model):
    message=models.TextField()
    #user
    #message
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)