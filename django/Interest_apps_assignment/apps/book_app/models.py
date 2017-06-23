from __future__ import unicode_literals
import re
from django.db import models
# from django.contrib import messages

# NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
class UserManager(models.Manager):
  def registration(self, postData):
    name = postData["name"]
    errors = []
    try:
      exists = User.objects.filter(name=name).exists()
      errors.append("name already exists")
      return [False, errors]

    except:
      u_name = User.objects.create(name=name)
      return [True, u_name]

class UserManager_interest(models.Manager):
  def inputInterest(self, postData):
    interest = postData["interest"]
    errors_interest = []
    try:
      exists = Interest.objects.filter(interest=interest).exists()
      errors_interest.append("interest already exists")
      return [False, errors_interest]

    except:
      u_interest = Interest.objects.create(interest=interest)
      return [True, u_interest]


class Interest(models.Model):
  interest = models.CharField(max_length=300, blank=True, null=True)
  created_at = models.DateTimeField(auto_now=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = UserManager_interest()

class User(models.Model):
  name = models.CharField(max_length=300, blank=True, null=True)
  created_at = models.DateTimeField(auto_now=True)
  updated_at = models.DateTimeField(auto_now=True)
  interests = models.ManyToManyField(Interest, related_name="users")
  objects = UserManager()


# this_interest = Interest.objects.get(id=1)
# this_user = User.objects.get(id=1)
# this_user.interests.add(this_interest)

  # def __unicode__(self):
  #   return "Username: " + str(self.username)
