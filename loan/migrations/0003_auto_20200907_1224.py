# Generated by Django 2.2.10 on 2020-09-07 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("loan", "0002_auto_20200907_1210"),
    ]

    operations = [
        migrations.AlterField(
            model_name="loan",
            name="applicantincome",
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name="loan",
            name="cooapplicantincome",
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name="loan",
            name="credit_history",
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name="loan",
            name="loan_amount_term",
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name="loan",
            name="loanamount",
            field=models.CharField(default=0, max_length=100),
        ),
    ]
