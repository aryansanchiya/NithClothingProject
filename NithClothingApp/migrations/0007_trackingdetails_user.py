# Generated by Django 3.2.12 on 2024-03-11 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NithClothingApp', '0006_auto_20240311_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackingdetails',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='NithClothingApp.user'),
        ),
    ]
