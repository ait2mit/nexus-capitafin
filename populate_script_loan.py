import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
import joblib
import django

django.setup()
from loan.models import (
    Gender,
    Married,
    Dependents,
    Education,
    Self_Employed,
    Property_Area,
)
import random
import numpy as np


def populate(data):
    # data is a list of lists

    for k, v in data.items():
        data_list = list(data[k])

        data_list = [x for x in data_list if str(x) != "nan"]

        for i, da in enumerate(data_list):
            id = 10 + i
            try:
                if k == "Gender":
                    Gender.objects.update_or_create(id=id, gender=da)
                elif k == "Married":
                    Married.objects.update_or_create(id=id, married=da)
                elif k == "Dependents":
                    Dependents.objects.update_or_create(id=id, dependents=da)

                elif k == "Education":
                    Education.objects.update_or_create(id=id, education=da)

                elif k == "Self_Employed":
                    Self_Employed.objects.update_or_create(id=id, self_employed=da)

                elif k == "Property_Area":
                    Property_Area.objects.update_or_create(id=id, property_area=da)
                else:
                    print("Not Necessary")
            except:
                print("Already Exist and continuing")
                continue

        print("Data Population for ***{}*** Successful".format(k))


if __name__ == "__main__":
    data = joblib.load(
        "ml-model-dev/loan-model/final-model-artifacts/categorical_values_for_dj_db.joblib"
    )
    print(data)
    populate(data)
