# Generated by Django 5.1.1 on 2024-09-27 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
