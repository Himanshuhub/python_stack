from __future__ import unicode_literals

from django.db import models

class CourseManager(models.Manager):
  def addCourse(self, postData):
    create = Course.objects.create(name=postData['name'], description=postDat['description'])
    return add_book, create

class Course(models.Model):
  name = models.CharField(max_length=38)
  description = models.CharField(max_length=38)
  created_at = models.DateTimeField(auto_now=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = CourseManager

  def __unicode__(self):
    return "id: " + str(self.id)+ " Name: "+ str(self.Name)+ "description: "+ str(self.description)
