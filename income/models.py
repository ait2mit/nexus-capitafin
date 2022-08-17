# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Workclass(models.Model):
    worktype = models.CharField(max_length=100, default="Private")

    def __str__(self):
        return "{}".format(self.worktype)


class Education(models.Model):
    edu = models.CharField(max_length=100, default="Bachelors")

    def __str__(self):
        return "{}".format(self.edu)


class Marital_Status(models.Model):
    ms = models.CharField(max_length=100, default="Never-married")

    def __str__(self):
        return "{}".format(self.ms)


class Relationship(models.Model):
    rel = models.CharField(max_length=100, default="Husband")

    def __str__(self):
        return "{}".format(self.rel)


class Occupation(models.Model):
    occ = models.CharField(max_length=100, default="Husband")

    def __str__(self):
        return "{}".format(self.occ)


class Race(models.Model):
    rc = models.CharField(max_length=100, default="White")

    def __str__(self):
        return "{}".format(self.rc)


class Sex(models.Model):
    sx = models.CharField(max_length=100, default="Female")

    def __str__(self):
        return "{}".format(self.sx)


class Native_Country(models.Model):
    nc = models.CharField(max_length=100, default="Canada")

    def __str__(self):
        return "{}".format(self.nc)


class Income(models.Model):
    income_id = models.IntegerField(primary_key=True)
    age = models.CharField(max_length=100, default=37)
    # workclass = models.CharField(max_length=100, default='Private')

    workclass = models.ForeignKey(Workclass, on_delete=models.CASCADE)

    fnlwgt = models.CharField(max_length=100, default=34146)
    # education = models.CharField(max_length=100, default="HS-grad")
    education = models.ForeignKey(Education, on_delete=models.CASCADE)

    education_num = models.CharField(max_length=100, default=9)
    # marital_status = models.CharField(max_length=100, default= "Married-civ-spouse")
    marital_status = models.ForeignKey(Marital_Status, on_delete=models.CASCADE)

    # occupation = models.CharField(max_length=100, default="Craft-repair")
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE)
    # relationship = models.CharField(max_length=100, default="Husband")
    relationship = models.ForeignKey(Relationship, on_delete=models.CASCADE)
    # race = models.CharField(max_length=100, default="White")
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    # sex = models.CharField(max_length=100, default="Male")
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE)
    capital_gain = models.CharField(max_length=100, default=0)
    capital_loss = models.CharField(max_length=100, default=0)
    hours_per_week = models.CharField(max_length=100, default=68)
    # native_country = models.CharField(max_length=100, default="United-States")
    native_country = models.ForeignKey(Native_Country, on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}".format(self.income_id, self.occupation)
