# Generated by Django 4.1.2 on 2022-10-26 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wep_app', '0008_cart_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='customer',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='orderby',
            name='customer',
            field=models.CharField(max_length=30, null=True),
        ),
    ]