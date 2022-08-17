# Generated by Django 2.2.10 on 2020-09-11 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("loan", "0004_auto_20200907_1235"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("eid", models.CharField(max_length=20)),
                ("ename", models.CharField(max_length=100)),
                ("eemail", models.EmailField(max_length=254)),
                ("econtact", models.CharField(max_length=15)),
            ],
            options={
                "db_table": "employee",
            },
        ),
    ]
