# -*- encoding: utf-8 -*-
"""
Copyright (c) 2022 - BengalAI
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "class": "form-control"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "class": "form-control"}
        )
    )

    # first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional')


    first_name = forms.CharField(
            widget=forms.TextInput(
                attrs={"placeholder": "First Name", "class": "form-control"}
            )

    )
    last_name = forms.CharField(
            widget=forms.TextInput(
                attrs={"placeholder": "Last Name", "class": "form-control"}
            )
    )










    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Email", "class": "form-control"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password check", "class": "form-control"}
        )
    )





    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("the given email is already registered")
        return self.cleaned_data['email']



    class Meta:
        model = User
        fields = ("username",  "first_name", "last_name",  "email", "password1", "password2")
