# Generated by Django 3.1.2 on 2020-12-11 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_tokey'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='is_interested',
            field=models.BooleanField(default=False, verbose_name='is interested'),
        ),
    ]
