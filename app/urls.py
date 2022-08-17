# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 - BengalAI
"""

from django.urls import path, re_path, include
from app import views

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    re_path(r"^.*\.html", views.pages, name="pages"),
    # The home page
    path("dash", views.index, name="home"),
]
