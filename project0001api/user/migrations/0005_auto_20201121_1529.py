# Generated by Django 3.0.11 on 2020-11-21 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20201116_0140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('badge_name', models.CharField(max_length=20)),
                ('badge_image', models.ImageField(upload_to='badges/')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='badges',
            field=models.ManyToManyField(related_name='users', to='user.Badge'),
        ),
    ]
