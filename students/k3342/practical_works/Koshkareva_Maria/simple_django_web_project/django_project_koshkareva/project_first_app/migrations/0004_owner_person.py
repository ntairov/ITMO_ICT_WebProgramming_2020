# Generated by Django 3.0.4 on 2020-06-17 20:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0003_auto_20200617_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='person',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
