from __future__ import unicode_literals
from django.db import models

# Create your models here.
class User(models.Model):
  first_name = models.CharField(max_length=45)
  last_name = models.CharField(max_length=45)
  email = models.CharField(max_length=45)
  password = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)

class Message(models.Model):
  title = models.CharField(max_length=45)
  message = models.TextField(max_length=1000)
  # Notice the association made with ForeignKey for a one-to-many relationship
		# There can be many posts to one User
  user_id = models.ForeignKey(User)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)

class Comment(models.Model):
  title = models.CharField(max_length=45)
  user_id = models.ForeignKey(User)
  message_id = models.ForeignKey(Message)
  comment = models.TextField(max_length=1000)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
