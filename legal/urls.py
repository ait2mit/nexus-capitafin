
from django.urls import path
from django.conf.urls import  include
from django.urls import re_path as url
from .views import privacy

urlpatterns = [
    path("privacy/", privacy, name="privacy"),

]
