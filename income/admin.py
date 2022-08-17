from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import (
    Income,
    Workclass,
    Education,
    Marital_Status,
    Relationship,
    Occupation,
    Race,
    Sex,
    Native_Country,
)

admin.site.register(Income)
admin.site.register(Workclass)
admin.site.register(Education)
admin.site.register(Marital_Status)
admin.site.register(Relationship)
admin.site.register(Occupation)
admin.site.register(Race)
admin.site.register(Sex)
admin.site.register(Native_Country)
