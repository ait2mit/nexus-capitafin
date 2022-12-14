# Generated by Django 3.1 on 2020-08-24 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dash", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Dash",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="dash/images/")),
                ("model_page", models.CharField(default="Model", max_length=100)),
                ("summary", models.CharField(default="Model", max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name="Job",
        ),
    ]
