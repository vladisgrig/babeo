from django.conf.urls import url
from programs import views

urlpatterns = [
    url(r'^(?:(?P<id>\d+)/)?$', views.index, name = "program-list"),
    url(r'^program/(?P<id>\d+)/$', views.program, name = "program")
]
