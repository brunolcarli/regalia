# Generated by Django 2.2.15 on 2022-04-06 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmw', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bmwoffer',
            name='date_reference',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]