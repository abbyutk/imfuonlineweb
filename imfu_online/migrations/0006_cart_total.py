# Generated by Django 3.1.1 on 2020-09-25 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imfu_online', '0005_auto_20200924_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.FloatField(null=True),
        ),
    ]
