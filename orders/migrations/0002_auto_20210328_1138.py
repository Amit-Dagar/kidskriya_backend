# Generated by Django 3.1.3 on 2021-03-28 06:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0f207b1a-8f8c-11eb-bfb8-acde48001122'), editable=False, primary_key=True, serialize=False),
        ),
    ]
