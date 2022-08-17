import os
import pandas as pd
import numpy as np
import joblib
import shap

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers

# from django.views.generic import ListView,CreateView, UpdateView, DeleteView
from django.views.generic import ListView, UpdateView, DeleteView
import pickle
import json, joblib
from .models import Loan
from .forms import LoanForm
from ml.loan_classifier.random_forest import RandomForestClassifier

from .models import (
    Loan,
    Gender,
    Married,
    Dependents,
    Education,
    Self_Employed,
    Property_Area,
)


# from .forms import *
from django.contrib.auth.decorators import login_required

# from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt

# from .models import PicPost

# Create your views here.
from ml.loan_classifier.random_forest import RandomForestClassifier

curr_wd = os.getcwd()


with open(
    "./ml-model-dev/loan-model/final-model-artifacts/features_list.csv", "rb"
) as fp:  # Unpickling
    model_fields = joblib.load(fp)

with open(
    "./ml-model-dev/loan-model/final-model-artifacts/features_list_lower.csv", "rb"
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


def loan(request):
    bma = Loan.objects.all()
    bma2 = Loan.objects.all()[0:2]
    if request.method == "POST":
        data = request.POST.get("str", "")
        obj = Loan.objects.all().filter(loan_id=data.upper())
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
        template_name="loan.html",
        context={"bma": bma, "model_fields": model_fields},
    )


def convert_fk_2_variables(qs_all_json):
    # This will convert categorical variable with foreign key links
    """
    Supporting functions which convert drop down variable id to variables in search
    """
    cat_var_lower = [
        "gender",
        "married",
        "dependents",
        "education",
        "self_employed",
        "property_area",
    ]
    cat = "gender"
    cat_fk = "{}_id".format(cat)
    fk_id = qs_all_json[0][cat_fk]
    qs_all_json[0][cat] = str(Gender.objects.get(pk=fk_id))

    cat = "married"
    cat_fk = "{}_id".format(cat)
    fk_id = qs_all_json[0][cat_fk]
    qs_all_json[0][cat] = str(Married.objects.get(pk=fk_id))

    cat = "dependents"
    cat_fk = "{}_id".format(cat)
    fk_id = qs_all_json[0][cat_fk]
    qs_all_json[0][cat] = str(Dependents.objects.get(pk=fk_id))

    cat = "education"
    cat_fk = "{}_id".format(cat)
    fk_id = qs_all_json[0][cat_fk]
    qs_all_json[0][cat] = str(Education.objects.get(pk=fk_id))

    cat = "self_employed"
    cat_fk = "{}_id".format(cat)
    fk_id = qs_all_json[0][cat_fk]
    qs_all_json[0][cat] = str(Self_Employed.objects.get(pk=fk_id))

    cat = "property_area"
    cat_fk = "{}_id".format(cat)
    fk_id = qs_all_json[0][cat_fk]
    qs_all_json[0][cat] = str(Property_Area.objects.get(pk=fk_id))

    return qs_all_json


def insert_data(request):
    template_name = "data_insert_loan.html"
    success_url = "/loan"
    scc_msg="Data has been saved to the database"
    if request.method == "POST":
        form = LoanForm(request.POST)
        args = {"loanform": form,"scc_msg":scc_msg}
        if form.is_valid():
            form.save()
            return render(request, template_name, args)

        else:
            form = LoanForm()
            args = {"loanform": form}
            return render(request, template_name, args)

    else:
        form = LoanForm()
        args = {"loanform": form}
        return render(request, template_name, args)


class DataUpdateView(UpdateView):
    model = Loan
    fields = model_fields_lower
    template_name = "data_update_loan.html"
    success_url = "/loan"

    def form_valid(self, form):
        return super().form_valid(form)


class DataDeleteView(DeleteView):
    model = Loan
    success_url = "/loan"
    template_name = "data_confirm_delete_loan.html"


def eval_process_loan(request):
    template_name = "evaluate_loan.html"
    form_data = request.POST.dict()
    form = LoanForm()
    if request.method == "POST":
        form_data = request.POST.dict()
        del form_data["csrfmiddlewaretoken"]
        del form_data["loan_id"]
        temp = {}
        temp["Gender"] = str(Gender.objects.get(pk=form_data["gender"]))
        temp["Married"] = str(Married.objects.get(pk=form_data["married"]))
        temp["Dependents"] = str(Dependents.objects.get(pk=form_data["dependents"]))
        temp["Education"] = str(Education.objects.get(pk=form_data["education"]))
        temp["Self_Employed"] = str(
            Self_Employed.objects.get(pk=form_data["self_employed"])
        )
        temp["ApplicantIncome"] = form_data["applicantincome"]
        temp["CoapplicantIncome"] = form_data["coapplicantincome"]
        temp["LoanAmount"] = form_data["loanamount"]
        temp["Loan_Amount_Term"] = form_data["loan_amount_term"]
        temp["Credit_History"] = form_data["credit_history"]
        temp["Property_Area"] = str(
            Property_Area.objects.get(pk=form_data["property_area"])
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
        file_decsion = "Approved" if file_score > test_threshold else "Declined"
        form_filled = LoanForm(request.POST)

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
        form = LoanForm()
        args = {"form": form}
        return render(request, template_name, args)

    args = {"form": form}

    return render(request, template_name, args)


def get_model_importance_df():
    df = pd.read_csv(
        "./ml-model-dev/loan-model/final-model-artifacts/model_importance_shap_df.csv"
    )

    df = df.iloc[::-1]
    model_shap_plot_data = {
        "labels": list(df.Variable.values),
        "chartdata": list(df.SHAP_abs.values),
        "corr_v": list(df.Corr.values),
    }

    return model_shap_plot_data


def get_processed_train_data(n_data_to_display):
    path_to_artifacts = curr_wd + "/ml-model-dev/loan-model/final-model-artifacts/"
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
    path_to_artifacts = curr_wd + "/ml-model-dev/loan-model/final-model-artifacts/"
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
        "./ml-model-dev/loan-model/final-model-artifacts/model_importance_shap_df.csv"
    )

    df = df.iloc[::-1]
    model_shap_plot_data = {
        "labels": list(df.Variable.values),
        "chartdata": list(df.SHAP_abs.values),
        "corr_v": list(df.Corr.values),
    }

    return model_shap_plot_data


class EvaluateLoan(UpdateView):
    """
    helps to evaluate view
    """

    model = Loan
    fields = model_fields_lower
    template_name = "evaluate_loan.html"
    success_url = "/loan"

    def form_valid(self, form):

        return super().form_valid(form)
