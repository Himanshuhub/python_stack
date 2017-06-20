from __future__ import unicode_literals

from django.db import models

class Book(models.Model):
  title = models.CharField(max_length=38)
  author = models.CharField(max_length=38)
  published_date = models.DateTimeField(auto_now_add=True)
  category = models.CharField(max_length=38)
  created_at = models.DateTimeField(auto_now=True)
  updated_at = models.DateTimeField(auto_now=True)
  in_print = models.BooleanField(True)

  # def __unicode__(self):
  #   return "id: " + str(self.id) + ", email: " + self.email
  #
