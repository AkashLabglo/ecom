# Generated by Django 4.1.2 on 2022-10-29 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wep_app', '0019_cart_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='date',
        ),
        migrations.RemoveField(
            model_name='orderby',
            name='date',
        ),
    ]