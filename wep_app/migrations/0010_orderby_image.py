# Generated by Django 4.1.2 on 2022-10-26 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wep_app', '0009_cart_customer_orderby_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderby',
            name='image',
            field=models.ImageField(null=True, upload_to='cart_img'),
        ),
    ]