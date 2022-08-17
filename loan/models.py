# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Gender(models.Model):
    gender = models.CharField(max_length=100, default="Male")

    def __str__(self):
        return "{}".format(self.gender)


class Married(models.Model):
    married = models.CharField(max_length=100, default="Yes")

    def __str__(self):
        return "{}".format(self.married)


class Dependents(models.Model):
    dependents = models.CharField(max_length=100, default="1")

    def __str__(self):
        return "{}".format(self.dependents)


class Education(models.Model):
    education = models.CharField(max_length=100, default="Graduate")

    def __str__(self):
        return "{}".format(self.education)


class Self_Employed(models.Model):
    self_employed = models.CharField(max_length=100, default="No")

    def __str__(self):
        return "{}".format(self.self_employed)


class Property_Area(models.Model):
    property_area = models.CharField(max_length=100, default="Rural")

    def __str__(self):
        return "{}".format(self.property_area)


class Loan(models.Model):
    loan_id = models.IntegerField(primary_key=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    married = models.ForeignKey(Married, on_delete=models.CASCADE)

    dependents = models.ForeignKey(Dependents, on_delete=models.CASCADE)
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    self_employed = models.ForeignKey(Self_Employed, on_delete=models.CASCADE)
    applicantincome = models.CharField(max_length=100, default=5000)
    coapplicantincome = models.CharField(max_length=100, default=10000)
    loanamount = models.CharField(max_length=100, default=10000)
    loan_amount_term = models.CharField(max_length=100, default=360)
    credit_history = models.CharField(max_length=100, default=1)
    property_area = models.ForeignKey(Property_Area, on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}".format(self.loan_id, self.education)
