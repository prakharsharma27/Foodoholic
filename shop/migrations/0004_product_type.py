# Generated by Django 4.0 on 2022-05-30 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_rename_subcategory_product_cuisine_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(default='', max_length=50),
        ),
    ]
