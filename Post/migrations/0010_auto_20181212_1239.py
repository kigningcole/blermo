# Generated by Django 2.1 on 2018-12-12 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0009_auto_20181212_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
