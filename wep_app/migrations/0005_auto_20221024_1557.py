# Generated by Django 3.2.12 on 2022-10-24 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wep_app', '0004_alter_cart_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orderby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax', models.DecimalField(decimal_places=2, max_digits=10)),
                ('original_price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('current_price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='prodect',
            name='model',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('dist', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=150)),
                ('pincode', models.IntegerField(null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wep_app.orderby')),
            ],
        ),
        migrations.AddField(
            model_name='orderby',
            name='prodect_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wep_app.prodect'),
        ),
    ]
