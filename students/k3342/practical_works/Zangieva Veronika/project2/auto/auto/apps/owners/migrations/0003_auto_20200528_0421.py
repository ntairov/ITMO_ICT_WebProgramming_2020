# Generated by Django 3.0.4 on 2020-05-28 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0002_auto_20200528_0359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ownership',
            name='owners',
        ),
        migrations.AddField(
            model_name='car',
            name='owners',
            field=models.ManyToManyField(through='owners.Ownership', to='owners.Owner'),
        ),
        migrations.AddField(
            model_name='ownership',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='owners.Owner'),
            preserve_default=False,
        ),
    ]
