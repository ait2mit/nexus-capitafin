# Generated by Django 2.2.10 on 2020-12-29 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('income', '0007_auto_20201229_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='marital_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='income.Marital_Status'),
        ),
        migrations.AlterField(
            model_name='income',
            name='native_country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='income.Native_Country'),
        ),
    ]
