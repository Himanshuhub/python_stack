from django.conf.urls import url
from . import views
urlpatterns = [
  url(r'^$', views.index),
  url(r'^add_course$', views.add_course),
  url(r'^delete/(?P<id>\d+)$', views.delete),
  url(r'^delete_course/(?P<id>\d+)$', views.delete_course),

]
