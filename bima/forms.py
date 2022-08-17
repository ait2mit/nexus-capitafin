from django import forms
from .models import Bima
from django.urls import reverse
import joblib
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div, Button

with open(
    "./ml-model-dev/bima-model/final-model-artifacts/features_list.csv", "rb"
) as fp:  # Unpickling
    model_fields = joblib.load(fp)

with open(
    "./ml-model-dev/bima-model/final-model-artifacts/features_list_lower.csv", "rb"
) as fp:  # Unpickling
    model_fields_lower = joblib.load(fp)


class BimaForm(forms.ModelForm):
    class Meta:
        model = Bima
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        model_field_names = model_fields_lower

        self.helper = FormHelper()

        self.helper.layout = Layout(
            Div(
                Div(model_field_names[0], css_class="col-sm-3"),
                Div(model_field_names[1], css_class="col-sm-3"),
                Div(model_field_names[2], css_class="col-sm-3"),
                Div(model_field_names[3], css_class="col-sm-3"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[4], css_class="col-sm-3"),
                Div(model_field_names[5], css_class="col-sm-3"),
                Div(model_field_names[6], css_class="col-sm-3"),
                Div(model_field_names[7], css_class="col-sm-3"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[8], css_class="col-sm-3"),
                Div(model_field_names[9], css_class="col-sm-3"),
                Div(model_field_names[10], css_class="col-sm-3"),
                Div(model_field_names[11], css_class="col-sm-3"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[12], css_class="col-sm-3"),
                Div(model_field_names[13], css_class="col-sm-3"),
                Div(model_field_names[14], css_class="col-sm-3"),
                Div(model_field_names[15], css_class="col-sm-3"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[16], css_class="col-sm-3"),
                Div(model_field_names[17], css_class="col-sm-3"),
                Div(model_field_names[18], css_class="col-sm-3"),
                Div(model_field_names[19], css_class="col-sm-3"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[20], css_class="col-sm-3"),
                Div(model_field_names[21], css_class="col-sm-3"),
                Div(model_field_names[22], css_class="col-sm-3"),
                Div(model_field_names[23], css_class="col-sm-3"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[24], css_class="col-sm-3"),
                Div(model_field_names[25], css_class="col-sm-3"),
                Div(model_field_names[26], css_class="col-sm-3"),
                Div(model_field_names[27], css_class="col-sm-3"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[28], css_class="col-sm-3"),
                Div(model_field_names[29], css_class="col-sm-3"),
                Div(model_field_names[30], css_class="col-sm-3"),
                Div(model_field_names[31], css_class="col-sm-3"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[32], css_class="col-sm-3"),
                Div(model_field_names[33], css_class="col-sm-3"),
                Div(model_field_names[34], css_class="col-sm-3"),
                Div(model_field_names[35], css_class="col-sm-3"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[36], css_class="col-sm-3"),
                Div(model_field_names[37], css_class="col-sm-3"),
                Div(model_field_names[38], css_class="col-sm-3"),
                Div(model_field_names[39], css_class="col-sm-3"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[40], css_class="col-sm-3"),
                Div(model_field_names[41], css_class="col-sm-3"),
                Div(model_field_names[42], css_class="col-sm-3"),
                Div(model_field_names[43], css_class="col-sm-3"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[44], css_class="col-sm-3"),
                Div(model_field_names[45], css_class="col-sm-3"),
                Div(model_field_names[46], css_class="col-sm-3"),
                Div(model_field_names[47], css_class="col-sm-3"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[48], css_class="col-sm-3"),
                Div(model_field_names[49], css_class="col-sm-3"),
                Div(model_field_names[50], css_class="col-sm-3"),
                Div(model_field_names[51], css_class="col-sm-3"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[52], css_class="col-sm-3"),
                Div(model_field_names[53], css_class="col-sm-3"),
                Div(model_field_names[54], css_class="col-sm-3"),
                Div(model_field_names[55], css_class="col-sm-3"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[56], css_class="col-sm-3"),
                Div(model_field_names[57], css_class="col-sm-3"),
                Div(model_field_names[58], css_class="col-sm-3"),
                Div(model_field_names[59], css_class="col-sm-3"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[60], css_class="col-sm-3"),
                Div(model_field_names[61], css_class="col-sm-3"),
                Div(model_field_names[62], css_class="col-sm-3"),
                Div(model_field_names[63], css_class="col-sm-3"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[64], css_class="col-sm-3"),
                Div(model_field_names[65], css_class="col-sm-3"),
                Div(model_field_names[66], css_class="col-sm-3"),
                Div(model_field_names[67], css_class="col-sm-3"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[68], css_class="col-sm-3"),
                Div(model_field_names[69], css_class="col-sm-3"),
                Div(model_field_names[70], css_class="col-sm-3"),
                Div(model_field_names[71], css_class="col-sm-3"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[72], css_class="col-sm-3"),
                Div(model_field_names[73], css_class="col-sm-3"),
                Div(model_field_names[74], css_class="col-sm-3"),
                Div(model_field_names[75], css_class="col-sm-3"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[76], css_class="col-sm-3"),
                Div(model_field_names[77], css_class="col-sm-3"),
                Div(model_field_names[78], css_class="col-sm-3"),
                Div(model_field_names[79], css_class="col-sm-3"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[80], css_class="col-sm-3"),
                Div(model_field_names[81], css_class="col-sm-3"),
                Div(model_field_names[82], css_class="col-sm-3"),
                Div(model_field_names[83], css_class="col-sm-3"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[84], css_class="col-sm-3"),
                Div(model_field_names[85], css_class="col-sm-3"),
                Div(model_field_names[86], css_class="col-sm-3"),
                Div(model_field_names[87], css_class="col-sm-3"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[88], css_class="col-sm-3"),
                Div(model_field_names[89], css_class="col-sm-3"),
                Div(model_field_names[90], css_class="col-sm-3"),
                Div(model_field_names[91], css_class="col-sm-3"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[92], css_class="col-sm-3"),
                Div(model_field_names[93], css_class="col-sm-3"),
                Div(model_field_names[94], css_class="col-sm-3"),
                Div(model_field_names[95], css_class="col-sm-3"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[96], css_class="col-sm-3"),
                Div(model_field_names[97], css_class="col-sm-3"),
                Div(model_field_names[98], css_class="col-sm-3"),
                Div(model_field_names[99], css_class="col-sm-3"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[100], css_class="col-sm-3"),
                Div(model_field_names[101], css_class="col-sm-3"),
                Div(model_field_names[102], css_class="col-sm-3"),
                Div(model_field_names[103], css_class="col-sm-3"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[104], css_class="col-sm-3"),
                Div(model_field_names[105], css_class="col-sm-3"),
                Div(model_field_names[106], css_class="col-sm-3"),
                Div(model_field_names[107], css_class="col-sm-3"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[108], css_class="col-sm-3"),
                Div(model_field_names[109], css_class="col-sm-3"),
                Div(model_field_names[110], css_class="col-sm-3"),
                Div(model_field_names[111], css_class="col-sm-3"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[112], css_class="col-sm-3"),
                Div(model_field_names[113], css_class="col-sm-3"),
                Div(model_field_names[114], css_class="col-sm-3"),
                Div(model_field_names[115], css_class="col-sm-3"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[116], css_class="col-sm-3"),
                Div(model_field_names[117], css_class="col-sm-3"),
                Div(model_field_names[118], css_class="col-sm-3"),
                Div(model_field_names[119], css_class="col-sm-3"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[120], css_class="col-sm-3"),
                Div(model_field_names[121], css_class="col-sm-3"),
                Div(model_field_names[122], css_class="col-sm-3"),
                Div(model_field_names[123], css_class="col-sm-3"),
                css_class="row",
            ),
            Div(
                Div(model_field_names[124], css_class="col-sm-3"),
                Div(model_field_names[125], css_class="col-sm-6"),
                Div(model_field_names[126], css_class="col-sm-6"),
                css_class="row",
            ),
        )
        self.helper.add_input(Submit("submit", "Submit", css_class="btn-primary"))
        self.helper.form_method = "post"
        self.helper.form_action = "insert-bima"
        self.helper.add_input(
            Button(
                "cancel",
                "Cancel",
                css_class="btn-primary",
                onclick="window.location.href = '{}';".format(reverse("bima")),
            )
        )
