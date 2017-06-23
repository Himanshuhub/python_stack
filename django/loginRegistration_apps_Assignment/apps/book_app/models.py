from __future__ import unicode_literals
import re
from django.db import models
# from django.contrib import messages

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
PW_REGEX = re.compile(r'^(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]$')

class UserManager(models.Manager):
  def registration(self, postData):
    # print "**********", postData
    firstname = postData["firstname"]
    lastname = postData["lastname"]
    email = postData["email"]
    password = postData["password"]
    birthday = postData["birthday"]
    errors = []

    if len(firstname)<2:
      errors.append("firstname is not long enough")
    if not NAME_REGEX.match(firstname):
      errors.append("firstname is incorrect")

    if len(lastname)<2:
      errors.append("lastname is not long enough")
    if not NAME_REGEX.match(lastname):
      errors.append("lastname is incorrect")

    if len(email)<1:
      errors.append("email is not long enough")
    if not EMAIL_REGEX.match(email):
      errors.append("email is incorrect")

    if len(password)<8:
      errors.append("password is not long enough")
    # if not PW_REGEX.match(password):
    #   errors.append("password is incorrect")

    # confirm_pw = postData['confirm_pw']
    # if confirm_pw != password:
    #   errors.append("password is not matching")

    exists = User.objects.filter(email=email).exists()
    if exists:
      errors.append("email exists, Ouch!!")
    if len(errors)==0:
      u = User.objects.create(firstname=firstname, lastname=lastname, email=email, password=password, birthday=birthday)
      return [True, u]
    else:
      return [False, errors]
    instance = User.objects.get(firstname=firstname, lastname=lastname, email=email, password=password, birthday=birthday)

class User(models.Model):
  firstname = models.CharField(max_length=300, blank=True, null=True)
  lastname = models.CharField(max_length=300, blank=True, null=True)
  email = models.CharField(max_length=300, blank=True, null=True)
  password = models.CharField(max_length=300, blank=True, null=True)
  birthday = models.CharField(max_length=300, blank=True, null=True)

  created_at = models.DateTimeField(auto_now=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = UserManager()

  # def __unicode__(self):
  #   return "Username: " + str(self.username)
