# Generated by Django 3.2.12 on 2024-03-11 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NithClothingApp', '0003_alter_order_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='size',
        ),
    ]
