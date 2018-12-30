# Generated by Django 2.1 on 2018-12-05 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_auto_20181205_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='follower',
        ),
        migrations.AddField(
            model_name='profile',
            name='follow',
            field=models.ManyToManyField(related_name='followed_by', to='users.Profile'),
        ),
    ]
