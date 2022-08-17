# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from django.views.generic import RedirectView  # shafi
from django.conf import settings
from django.conf.urls.static import static

from endpoints.urls import urlpatterns as endpoints_urlpatterns
import app.views
import income.views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("authentication.urls")),  # add this
    path("", include("dash.urls")),  # add this
    path("", include("app.urls")),  # add this
    path("", include("income.urls")),  # add this
    path("", include("loan.urls")),  # add this
    path("", include("bima.urls")),  # add this
    path("", include("contact.urls")),  # add this
    path("", include("legal.urls")),  # add this
    path("", include("eda.urls")),  # add this
    #path("", include("form_app.urls")),  # add this
    #path("", include("student_task.urls")),  # add this
    # path('income',income.views.income, name='income'),
    # path('evalModel',income.views.evalModel, name='evalModel'),
    # path('api', income.views.ChartData.as_view()),
]
# Shafi below


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


"""
urlpatterns = [
    path('admin/', admin.site.urls),
]
"""
# Model API End Points
urlpatterns += endpoints_urlpatterns
