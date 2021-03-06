# Generated by Django 3.1.3 on 2021-03-24 06:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schools', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.UUIDField(default=190070690681122, editable=False, primary_key=True, serialize=False)),
                ('price', models.FloatField()),
                ('status', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.schools')),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.classes')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='OrderProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_price', models.FloatField()),
                ('discount', models.IntegerField()),
                ('banner', models.CharField(max_length=800)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.orders')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'order_products',
            },
        ),
    ]
