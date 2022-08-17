
from django.urls import path
from django.conf.urls import url
from .views import privacy

urlpatterns = [
    path("privacy/", privacy, name="privacy"),

]
