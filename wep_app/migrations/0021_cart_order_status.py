# Generated by Django 4.1.2 on 2022-10-30 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wep_app', '0020_remove_cart_date_remove_orderby_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='order_status',
            field=models.CharField(default='new_order', max_length=40),
        ),
    ]
