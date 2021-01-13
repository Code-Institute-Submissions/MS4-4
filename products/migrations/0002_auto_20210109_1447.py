# Generated by Django 3.1.5 on 2021-01-09 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='colour',
        ),
        migrations.AddField(
            model_name='category',
            name='reuseable',
            field=models.BooleanField(default=True),
        ),
    ]
