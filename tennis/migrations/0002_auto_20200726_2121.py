# Generated by Django 3.0.8 on 2020-07-26 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tennis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tennisevent',
            name='match_id',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
