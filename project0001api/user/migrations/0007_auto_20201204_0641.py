# Generated by Django 3.0.11 on 2020-12-04 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20201122_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='badges',
        ),
        migrations.DeleteModel(
            name='Badge',
        ),
    ]
