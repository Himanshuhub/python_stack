from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
  def validations(self, postData):
    print "**********", postData
    username = postData["username"]
    errors = []
    if len(username)<8:
      errors.append("username is not long enough, Ouch!!")
    if len(username)>26:
      errors.append("username is too long, Ouch!!")
    exists = User.objects.filter(username=username).exists
    if exists:
        errors.append("Already exists")

    if len(errors)==0:
      u = User.objects.create(username=username)
      return [True, u]
    else:
      return [False, errors]

class User(models.Model):
  username = models.CharField(max_length=38)
  # description = models.CharField(max_length=38)
  created_at = models.DateTimeField(auto_now=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = UserManager()

  def __unicode__(self):
    return "Username: " + str(self.username)
