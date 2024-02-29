# Generated by Django 3.2.12 on 2023-12-29 09:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NithClothingApp', '0005_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='admin_drop_link',
            name='DateTime',
            field=models.DateField(default=datetime.date(2023, 12, 29)),
        ),
    ]
