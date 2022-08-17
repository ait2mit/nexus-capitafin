
from django.urls import path
from django.conf.urls import url
from .views import contact


urlpatterns = [
    path("contact/", contact, name="contact"),

]
