from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
url(r'^$', views.index),     # This line has changed!
url(r'^testimonials$', views.testimonials),
url(r'^aboutme$', views.aboutme),
url(r'^projects$', views.projects),
url(r'^new_user$', views.create)
]
