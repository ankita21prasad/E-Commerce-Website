# Generated by Django 3.0.7 on 2020-07-20 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default=9516995213, max_length=50),
            preserve_default=False,
        ),
    ]
