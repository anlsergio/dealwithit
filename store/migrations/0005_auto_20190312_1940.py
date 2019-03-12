# Generated by Django 2.1.7 on 2019-03-12 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='expiration_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='is_expired',
            field=models.BooleanField(default=False),
        ),
    ]
