from django.db import models
import os
# Create your models here.
class Dash(models.Model):
    d = os.getcwd() # how we get the current dorectory
    print("d = os.getcwd() # how we get the current dorectory", d)

    image = models.ImageField(upload_to="images")
    model_page = models.CharField(max_length=100, default="Model")
    summary = models.CharField(max_length=200, default="Model")

    def __str__(self):
        return "{}".format(self.summary)
