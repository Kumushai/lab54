# Generated by Django 4.2.2 on 2023-07-04 08:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_product_balance_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='balance',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Остаток'),
        ),
    ]
