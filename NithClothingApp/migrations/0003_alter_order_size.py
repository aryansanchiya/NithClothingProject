# Generated by Django 3.2.12 on 2024-03-11 12:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('NithClothingApp', '0002_alter_order_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='size',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
