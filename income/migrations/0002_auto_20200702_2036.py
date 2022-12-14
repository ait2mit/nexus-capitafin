# Generated by Django 3.0.7 on 2020-07-02 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("income", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="income",
            name="age",
            field=models.CharField(default=37, max_length=100),
        ),
        migrations.AlterField(
            model_name="income",
            name="capital_gain",
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name="income",
            name="capital_loss",
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name="income",
            name="education",
            field=models.CharField(default="HS-grad", max_length=100),
        ),
        migrations.AlterField(
            model_name="income",
            name="education_num",
            field=models.CharField(default=9, max_length=100),
        ),
        migrations.AlterField(
            model_name="income",
            name="fnlwgt",
            field=models.CharField(default=34146, max_length=100),
        ),
        migrations.AlterField(
            model_name="income",
            name="hours_per_week",
            field=models.CharField(default=68, max_length=100),
        ),
        migrations.AlterField(
            model_name="income",
            name="marital_status",
            field=models.CharField(default="Married-civ-spouse", max_length=100),
        ),
        migrations.AlterField(
            model_name="income",
            name="native_country",
            field=models.CharField(default="United-States", max_length=100),
        ),
        migrations.AlterField(
            model_name="income",
            name="occupation",
            field=models.CharField(default="Craft-repair", max_length=100),
        ),
        migrations.AlterField(
            model_name="income",
            name="race",
            field=models.CharField(default="White", max_length=100),
        ),
        migrations.AlterField(
            model_name="income",
            name="relationship",
            field=models.CharField(default="Husband", max_length=100),
        ),
        migrations.AlterField(
            model_name="income",
            name="sex",
            field=models.CharField(default="Male", max_length=100),
        ),
        migrations.AlterField(
            model_name="income",
            name="workclass",
            field=models.CharField(default="Private", max_length=100),
        ),
    ]
