# Generated by Django 3.0.3 on 2021-06-29 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_auto_20210626_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_history',
            name='release_date',
            field=models.DateField(null=True, verbose_name='Release Date'),
        ),
    ]