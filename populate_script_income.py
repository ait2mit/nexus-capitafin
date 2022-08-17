import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
import joblib
import django

django.setup()
from income.models import (
    Workclass,
    Education,
    Marital_Status,
    Relationship,
    Occupation,
    Race,
    Sex,
    Native_Country,
)
import random
import numpy as np



def populate(data):
    # data is a list of lists
    data_list = [
        "Never-worked",
        "Self-emp-inc",
        "Self-emp-not-inc",
        "State-gov",
        "Local-gov",
        "Without-pay",
        "Federal-gov",
        "Private",
    ]
    for k, v in data.items():
        data_list = list(data[k])

        data_list = [x for x in data_list if str(x) != "nan"]

        for i, da in enumerate(data_list):
            id = 10 + i

            if k == "workclass":
                Workclass.objects.get_or_create(id=id, worktype=da)
            elif k == "education":
                Education.objects.get_or_create(id=id, edu=da)
            elif k == "marital-status":
                Marital_Status.objects.get_or_create(id=id, ms=da)

            elif k == "relationship":
                Relationship.objects.get_or_create(id=id, rel=da)

            elif k == "occupation":
                Occupation.objects.get_or_create(id=id, occ=da)

            elif k == "race":
                Race.objects.get_or_create(id=id, rc=da)
            elif k == "sex":
                Sex.objects.get_or_create(id=id, sx=da)

            elif k == "native-country":
                Native_Country.objects.get_or_create(id=id, nc=da)
            else:
                print("Not Necessary")

        print("Data Population Successful")


if __name__ == "__main__":
    data = joblib.load(
        "ml-model-dev/income-model/final-model-artifacts/categorical_values_for_dj_db.pkl"
    )
    print(data)
    populate(data)
