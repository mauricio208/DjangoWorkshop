# Generated by Django 2.1.1 on 2018-09-21 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphmaker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='childs',
            field=models.ManyToManyField(to='graphmaker.Account'),
        ),
    ]