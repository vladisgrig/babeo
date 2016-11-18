from django.conf.urls import url
from userManagementApp import views

urlpatterns = [
    url(r'^$', views.login_page, name = "login_page"),
    url(r'^reg/$', views.reg_page, name = "registration_page"),
    url(r'^login/$', views.login, name = "login"),
    url(r'^logout/$', views.logout, name = "logout"),
    url(r'^registration/$', views.registration, name = "registration"),
]
