# Generated by Django 2.1.7 on 2019-02-27 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20190227_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number_is_public',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]