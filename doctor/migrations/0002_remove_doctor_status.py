# Generated by Django 3.0.3 on 2021-07-05 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='status',
        ),
    ]
