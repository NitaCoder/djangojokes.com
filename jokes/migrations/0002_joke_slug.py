# Generated by Django 5.0 on 2023-12-13 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='joke',
            name='slug',
            field=models.SlugField(editable=False, null=True, unique=True),
        ),
    ]
