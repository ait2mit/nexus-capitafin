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
from .models import Bima
from .forms import BimaForm

# from .forms import *
from django.contrib.auth.decorators import login_required

# from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt

# from .models import PicPost

# Create your views here.
from ml.bima_classifier.random_forest import RandomForestClassifier

curr_wd = os.getcwd()


with open(
    "./ml-model-dev/bima-model/final-model-artifacts/features_list.csv", "rb"
) as fp:  # Unpickling
    model_fields = joblib.load(fp)

with open(
    "./ml-model-dev/bima-model/final-model-artifacts/features_list_lower.csv", "rb"
) as fp:  # Unpickling
    model_fields_lower = joblib.load(fp)


@login_required(login_url="/login/")
def bima(request):
    bma = Bima.objects.all()
    bma2 = Bima.objects.all()[0:2]
    if request.method == "POST":
        data = request.POST.get("str", "")
        obj = Bima.objects.all().filter(id=data.upper())
        if obj.exists():
            # all_points = bma2 | obj # Union
            all_points = obj
            qs_all_json = list(all_points.values())
            reply = json.dumps(qs_all_json, sort_keys=True)
            return HttpResponse(reply)
        else:

            return HttpResponse("Not Found")
    else:

        return render(
            request=request,
            template_name="bima.html",
            context={"bma": bma, "model_fields": model_fields},
        )


@login_required(login_url="/login/")
def insert_data(request):
    template_name = "data_insert_bima.html"
    scc_msg="Data has been saved to the database"
    success_url = "/bima"
    if request.method == "POST":
        form = BimaForm(request.POST)
        args = {"bimaform": form,"scc_msg":scc_msg}
        if form.is_valid():
            form.save()

            return render(request, template_name, args)
        else:
            form = BimaForm()
            args = {"bimaform": form}
            return render(request, template_name, args)
    else:
        form = BimaForm()
        args = {"bimaform": form}
        return render(request, template_name, args)


class DataUpdateView(UpdateView):
    model = Bima
    fields = model_fields_lower
    template_name = "data_update_bima.html"
    success_url = "/bima"

    def form_valid(self, form):
        return super().form_valid(form)


class DataDeleteView(DeleteView):
    model = Bima
    success_url = "/bima"
    template_name = "data_confirm_delete_bima.html"


def eval_process_bima(request):
    template_name = "evaluate_bima.html"
    form_data = request.POST.dict()
    form = BimaForm()
    if request.method == "POST":
        form_data = request.POST.dict()
        del form_data["csrfmiddlewaretoken"]
        del form_data["id"]
        temp = {}
        for f in model_fields[1:]:  # exclude Id
            temp[f] = form_data[f.lower()]

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
        form_filled = BimaForm(request.POST)

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
        form = BimaForm()
        args = {"form": form}
        return render(request, template_name, args)

    args = {"form": form}

    return render(request, template_name, args)


def get_model_importance_df():
    df = pd.read_csv(
        "./ml-model-dev/bima-model/final-model-artifacts/model_importance_shap_df.csv"
    )

    df = df.iloc[::-1]
    model_shap_plot_data = {
        "labels": list(df.Variable.values),
        "chartdata": list(df.SHAP_abs.values),
        "corr_v": list(df.Corr.values),
    }

    return model_shap_plot_data


def get_processed_train_data(n_data_to_display):
    path_to_artifacts = curr_wd + "/ml-model-dev/bima-model/final-model-artifacts/"
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
    path_to_artifacts = curr_wd + "/ml-model-dev/bima-model/final-model-artifacts/"
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
        "./ml-model-dev/bima-model/final-model-artifacts/model_importance_shap_df.csv"
    )

    df = df.iloc[::-1]
    model_shap_plot_data = {
        "labels": list(df.Variable.values),
        "chartdata": list(df.SHAP_abs.values),
        "corr_v": list(df.Corr.values),
    }

    return model_shap_plot_data


class EvaluateBima(UpdateView):
    """
    helps to evaluate view
    """

    model = Bima
    fields = model_fields_lower
    template_name = "evaluate_bima.html"
    success_url = "/bima"

    def form_valid(self, form):

        return super().form_valid(form)
