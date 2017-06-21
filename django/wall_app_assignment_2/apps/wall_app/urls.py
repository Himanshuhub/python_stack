from django.conf.urls import url
from . import views
url_patterns = [
  url(r'^$', views.index, name="index"),
  # url(r'^blogs$', views.blogs),
]
