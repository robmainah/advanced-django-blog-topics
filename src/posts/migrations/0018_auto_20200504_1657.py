# Generated by Django 2.1 on 2020-05-04 13:57

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0017_auto_20200504_1633'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostTopic',
            new_name='Post',
        ),
    ]