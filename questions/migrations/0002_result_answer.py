# Generated by Django 3.2.5 on 2021-07-22 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='answer',
            field=models.IntegerField(default=0),
        ),
    ]