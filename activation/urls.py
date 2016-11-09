from django.conf.urls import url
from activation import views

urlpatterns = [
    url(r'^$', views.activate_sertificate, name = "activate_sertificate"),
    url(r'^success/$', views.return_success_message, name = "success_activation"),
    url(r'^unsuccess/$', views.return_unsuccess_message, name = "unsuccess_activation"),
    url(r'^outdated/$', views.return_outdated_message, name = "outdated_activation"),    

]
