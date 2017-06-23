from django.conf.urls import url
from . import views
urlpatterns = [
  url(r'^$', views.index),
  url(r'^success$', views.success),
  url(r'^add_username$', views.add_username),
  # url(r'^delete/(?P<id>\d+)$', views.delete),
  # url(r'^delete_course/(?P<id>\d+)$', views.delete_course),
]
