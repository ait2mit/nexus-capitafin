import os
import pandas as pd
import numpy as np
import joblib
import shap

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

##Shafi
from .forms import IncomeForm
from ml.income_classifier.random_forest import RandomForestClassifier

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
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404


from django.views.generic import ListView, UpdateView, DeleteView
import pandas as pd
import numpy as np
import joblib
import shap

import pickle


curr_wd = os.getcwd()


with open(
    "./ml-model-dev/income-model/final-model-artifacts/features_list.csv", "rb"
) as fp:  # Unpickling
    model_fields = joblib.load(fp)

with open(
    "./ml-model-dev/income-model/final-model-artifacts/features_list_lower.csv", "rb"
) as fp:  # Unpickling
    model_fields_lower = joblib.load(fp)

cat_var_lower = [
    "gender",
    "married",
    "dependents",
    "education",
    "self_employed",
    "property_area",
]


def income(request):
    bma = Income.objects.all()
    bma2 = Income.objects.all()[0:2]
    if request.method == "POST":
        data = request.POST.get("str", "")
        obj = Income.objects.all().filter(income_id=data.upper())
        if obj.exists():
            # all_points = bma2 | obj # Union
            all_points = obj

            qs_all_json = list(all_points.values())

            # This will convert categorical variable with foreign key links
            qs_all_json = convert_fk_2_variables(qs_all_json)

            reply = json.dumps(qs_all_json, sort_keys=True)

            return HttpResponse(reply)
        else:
            return HttpResponse("Not Found")
    else:
        pass

    # return HttpResponse(bma)
    return render(
        request=request,
        template_name="income.html",
        context={"bma": bma, "model_fields": model_fields},
    )


def convert_fk_2_variables(qs_all_json):
    # This will convert categorical variable with foreign key links
    """
    Supporting functions which convert drop down variable id to variables in search
    """

    cat = "Workclass".lower()
    cat_fk = "{}_id".format(cat)
    fk_id = qs_all_json[0][cat_fk]
    qs_all_json[0][cat] = str(Workclass.objects.get(pk=fk_id))

    cat = "Education".lower()
    cat_fk = "{}_id".format(cat)
    fk_id = qs_all_json[0][cat_fk]
    qs_all_json[0][cat] = str(Education.objects.get(pk=fk_id))

    cat = "Marital_Status".lower()
    cat_fk = "{}_id".format(cat)
    fk_id = qs_all_json[0][cat_fk]
    qs_all_json[0][cat] = str(Marital_Status.objects.get(pk=fk_id))

    cat = "Occupation".lower()
    cat_fk = "{}_id".format(cat)
    fk_id = qs_all_json[0][cat_fk]
    qs_all_json[0][cat] = str(Occupation.objects.get(pk=fk_id))

    cat = "Relationship".lower()
    cat_fk = "{}_id".format(cat)
    fk_id = qs_all_json[0][cat_fk]
    qs_all_json[0][cat] = str(Relationship.objects.get(pk=fk_id))

    cat = "Race".lower()
    cat_fk = "{}_id".format(cat)
    fk_id = qs_all_json[0][cat_fk]
    qs_all_json[0][cat] = str(Race.objects.get(pk=fk_id))

    cat = "Sex".lower()
    cat_fk = "{}_id".format(cat)
    fk_id = qs_all_json[0][cat_fk]
    qs_all_json[0][cat] = str(Sex.objects.get(pk=fk_id))

    cat = "Native_Country".lower()
    cat_fk = "{}_id".format(cat)
    fk_id = qs_all_json[0][cat_fk]
    qs_all_json[0][cat] = str(Native_Country.objects.get(pk=fk_id))

    return qs_all_json


def insert_data(request):
    template_name = "data_insert_income.html"
    success_url = "/income"
    scc_msg="Data has been saved to the database"
    if request.method == "POST":
        form = IncomeForm(request.POST)
        args = {"incomeform": form,"scc_msg":scc_msg}
        if form.is_valid():
            form.save()
            return render(request, template_name, args)
        else:
            form = IncomeForm()
            args = {"incomeform": form}
            return render(request, template_name, args)
    else:
        form = IncomeForm()
        args = {"incomeform": form}
        return render(request, template_name, args)


class DataUpdateView(UpdateView):
    model = Income
    fields = model_fields_lower
    template_name = "data_update_income.html"
    success_url = "/income"

    def form_valid(self, form):
        return super().form_valid(form)


class DataDeleteView(DeleteView):
    model = Income
    success_url = "/income"
    template_name = "data_confirm_delete_income.html"


def eval_process_income(request):
    template_name = "evaluate_income.html"
    form_data = request.POST.dict()
    form = IncomeForm()

    if request.method == "POST":
        form_data = request.POST.dict()
        del form_data["csrfmiddlewaretoken"]
        del form_data["income_id"]


        temp = {}

        temp["Age"] = form_data["age"]
        temp["Workclass"] = str(Workclass.objects.get(pk=form_data["workclass"]))
        temp["Fnlwgt"] = form_data["fnlwgt"]
        temp["Education"] = str(Education.objects.get(pk=form_data["education"]))
        temp["Education_Num"] = form_data["education_num"]
        temp["Marital_Status"] = str(
            Marital_Status.objects.get(pk=form_data["marital_status"])
        )
        temp["Occupation"] = str(Occupation.objects.get(pk=form_data["occupation"]))
        temp["Relationship"] = str(
            Relationship.objects.get(pk=form_data["relationship"])
        )
        temp["Race"] = str(Race.objects.get(pk=form_data["race"]))
        temp["Sex"] = str(Sex.objects.get(pk=form_data["sex"]))
        temp["Capital_Gain"] = form_data["capital_gain"]
        temp["Capital_Loss"] = form_data["capital_loss"]
        temp["Hours_Per_Week"] = form_data["hours_per_week"]
        temp["Native_Country"] = str(
            Native_Country.objects.get(pk=form_data["native_country"])
        )

        model_shap_plot_data = get_model_importance_df()
        cols, shap_probs = get_shap_probs(temp)

        n_data_to_display = 6
        train_probs = get_processed_train_data(n_data_to_display)
        auc = 0.98
        test_threshold = 0.52
        showPlot = "True"
        pred = RandomForestClassifier().compute_prediction(temp)
        file_score = pred["probability"]
        file_decsion = ">50K" if file_score > test_threshold else "<=50K"
        form_filled = IncomeForm(request.POST)

        args = {
            "form": form_filled,
            "prediction": pred,
            "model_shap_plot_data": model_shap_plot_data,
            "showPlot": showPlot,
            "auc": auc,
            "test_threshold": test_threshold,
            "scoreF": file_score,
            "file_decsion": file_decsion,
            "shap_cols": cols,
            "shap_probs": shap_probs,
            "train_probs": train_probs,
        }


        return render(request, template_name, args)

    else:
        form = IncomeForm()
        args = {"form": form}
        return render(request, template_name, args)

    args = {"form": form}

    return render(request, template_name, args)


def get_model_importance_df():
    df = pd.read_csv(
        "./ml-model-dev/income-model/final-model-artifacts/model_importance_shap_df.csv"
    )

    df = df.iloc[::-1]
    model_shap_plot_data = {
        "labels": list(df.Variable.values),
        "chartdata": list(df.SHAP_abs.values),
        "corr_v": list(df.Corr.values),
    }

    return model_shap_plot_data


def get_processed_train_data(n_data_to_display):
    path_to_artifacts = curr_wd + "/ml-model-dev/income-model/final-model-artifacts/"
    df_good = pd.read_csv(
        path_to_artifacts + "good_200_row_data.csv", nrows=n_data_to_display - 1
    )  # 1 to include specific file
    df_good = df_good.drop(
        df_good.columns.values[-1], axis=1
    )  # This not model income it it data income

    train_probs = []
    for ind in df_good.index.values:
        new_temp = {}
        temp_row = df_good.loc[ind].to_dict()
        # maker sure all elements are strings
        for k, v in temp_row.items():
            new_temp[k] = str(v)

        _, probs_row = get_shap_probs(new_temp)
        train_probs.append(probs_row)
    return train_probs


def get_shap_probs(temp):
    path_to_artifacts = curr_wd + "/ml-model-dev/income-model/final-model-artifacts/"
    model = joblib.load(path_to_artifacts + "random_forest_model.joblib")
    explainer = shap.TreeExplainer(model)
    expected_value = explainer.expected_value

    features = RandomForestClassifier().preprocessing(temp)

    cols = list(features.columns)
    shap_values = explainer.shap_values(features)[1]

    e = expected_value[0]

    shap_probs = [
        round(np.exp((c + e)) / (1 + np.exp(c + e)), 3) for c in shap_values[0]
    ]

    return cols, shap_probs


def get_model_importance_df():
    df = pd.read_csv(
        "./ml-model-dev/income-model/final-model-artifacts/model_importance_shap_df.csv"
    )

    df = df.iloc[::-1]
    model_shap_plot_data = {
        "labels": list(df.Variable.values),
        "chartdata": list(df.SHAP_abs.values),
        "corr_v": list(df.Corr.values),
    }

    return model_shap_plot_data


class EvaluateIncome(UpdateView):
    """
    helps to evaluate view
    """

    model = Income
    fields = model_fields_lower
    template_name = "evaluate_income.html"
    success_url = "/income"

    def form_valid(self, form):

        return super().form_valid(form)
