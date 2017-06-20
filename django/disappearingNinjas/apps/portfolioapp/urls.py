from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
url(r'^$', views.index),     # This line has changed!
url(r'^ninjas$', views.ninjas),
# url(r'^aboutme$', views.aboutme),
# url(r'^projects$', views.projects),
# url(r'^new_user$', views.create),
url(r'^ninjas/(?P<color>[a-z]+)$', views.show)
]
