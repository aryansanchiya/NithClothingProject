# Generated by Django 3.2.12 on 2023-12-29 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NithClothingApp', '0006_auto_20231229_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
