"""lumos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import  include
from django.urls import re_path as url
from . import views
from .views import DataUpdateView, DataDeleteView, EvaluateBima

# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path("bima", views.bima, name="bima"),
    path("data/insert-bima/", views.insert_data, name="insert-bima"),
    path(
        "data/<int:pk>/update-bima/", DataUpdateView.as_view(), name="data-update-bima"
    ),
    path(
        "data/<int:pk>/delete-bima/", DataDeleteView.as_view(), name="data-delete-bima"
    ),
    path(
        "data/<int:pk>/evaluate-bima/", EvaluateBima.as_view(), name="evaluate-bima"
    ),  # This one works as view as per pk
    path(
        "data/eval_process_bima/", views.eval_process_bima, name="eval_process_bima"
    ),  # View after Process
]
