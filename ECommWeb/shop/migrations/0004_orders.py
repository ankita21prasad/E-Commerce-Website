# Generated by Django 3.0.7 on 2020-07-20 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=6)),
            ],
        ),
    ]
