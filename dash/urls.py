from django.urls import path

from . import views

urlpatterns = [
    # path('sarina.html', views.sarina_page, name='sarina'),
    path("", views.ai_dash, name="dash"),
]
