# Generated by Django 3.2.12 on 2022-10-28 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wep_app', '0014_prodect_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prodect',
            name='added',
            field=models.CharField(max_length=150),
        ),
    ]
