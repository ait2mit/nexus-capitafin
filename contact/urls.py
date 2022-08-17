
from django.urls import path
from django.conf.urls import  include
from django.urls import re_path as url
from .views import contact


urlpatterns = [
    path("contact/", contact, name="contact"),

]
