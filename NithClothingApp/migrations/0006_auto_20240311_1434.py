# Generated by Django 3.2.12 on 2024-03-11 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NithClothingApp', '0005_orderitem_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='trackinglink',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='trackingno',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
