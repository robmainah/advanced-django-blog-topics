# Generated by Django 2.1 on 2020-04-23 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200423_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posttopic',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
