from django.shortcuts import render
from .models import Dash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader

# Create your views here.


@login_required(login_url="/login/")
def ai_dash(request):
    dash = Dash.objects
    return render(request, "dash.html", {"dash": dash})
