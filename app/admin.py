# -*- encoding: utf-8 -*-
"""

Copyright (c) 2022 - BengalAI
"""

from django.contrib import admin

# Register your models here.
from .models import Pizza, Size

admin.site.register(Pizza)
admin.site.register(Size)
