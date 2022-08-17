from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import (
    Loan,
    Gender,
    Married,
    Dependents,
    Education,
    Self_Employed,
    Property_Area,
)

admin.site.register(Loan)
admin.site.register(Gender)
admin.site.register(Married)
admin.site.register(Dependents)
admin.site.register(Education)
admin.site.register(Self_Employed)
admin.site.register(Property_Area)
