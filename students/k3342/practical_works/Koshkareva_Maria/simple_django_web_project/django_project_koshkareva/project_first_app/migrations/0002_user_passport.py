# Generated by Django 3.0.4 on 2020-06-17 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='passport',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
