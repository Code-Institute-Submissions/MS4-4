# Generated by Django 3.1.5 on 2021-01-13 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210109_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='reuseable',
        ),
        migrations.AddField(
            model_name='product',
            name='colour',
            field=models.CharField(max_length=254, null=True),
        ),
    ]