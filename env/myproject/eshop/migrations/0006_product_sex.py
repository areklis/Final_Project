# Generated by Django 3.2.7 on 2021-09-23 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0005_rename_name_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sex',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
