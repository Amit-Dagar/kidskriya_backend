# Generated by Django 3.1.3 on 2021-05-13 16:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20210513_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='id',
            field=models.UUIDField(default=uuid.UUID('584c3348-b406-11eb-bcb9-ac1203cf8108'), editable=False, primary_key=True, serialize=False),
        ),
    ]