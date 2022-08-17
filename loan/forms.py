from django import forms
from .models import Loan
from django.urls import reverse
import joblib
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, Button


with open(
    "./ml-model-dev/loan-model/final-model-artifacts/features_list.csv", "rb"
) as fp:  # Unpickling
    model_fields = joblib.load(fp)

with open(
    "./ml-model-dev/loan-model/final-model-artifacts/features_list_lower.csv", "rb"
) as fp:  # Unpickling
    model_fields_lower = joblib.load(fp)


class LoanForm(forms.ModelForm):
    # image = forms.ImageField()
    class Meta:
        model = Loan
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        model_field_names = model_fields_lower

        self.helper = FormHelper()

        self.helper.layout = Layout(
            Div(
                Div(model_field_names[0], css_class="col-sm-4"),
                Div(model_field_names[1], css_class="col-sm-4"),
                Div(model_field_names[2], css_class="col-sm-4"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[3], css_class="col-sm-4"),
                Div(model_field_names[4], css_class="col-sm-4"),
                Div(model_field_names[5], css_class="col-sm-4"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[6], css_class="col-sm-4"),
                Div(model_field_names[7], css_class="col-sm-4"),
                Div(model_field_names[8], css_class="col-sm-4"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[9], css_class="col-sm-4"),
                Div(model_field_names[10], css_class="col-sm-4"),
                Div(model_field_names[11], css_class="col-sm-4"),
                css_class="row",
            ),
        )
        self.helper.add_input(Submit("submit", "Submit", css_class="btn-primary"))
        self.helper.form_method = "post"
        self.helper.form_action = "insert-loan"
        self.helper.add_input(
            Button(
                "cancel",
                "Cancel",
                css_class="btn-primary",
                onclick="window.location.href = '{}';".format(reverse("loan")),
            )
        )
