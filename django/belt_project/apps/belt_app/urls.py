from django.conf.urls import url
from . import views
from IPython import embed
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),

    url(r'^books$', views.books),
    url(r'^books/add$', views.add),
    url(r'^users$', views.users),

    url(r'^user/(?P<userid>\d+)$', views.user),
    url(r'^book/(?P<bookid>\d+)$', views.book),

]
