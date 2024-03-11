# Generated by Django 3.2.12 on 2024-03-11 11:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AdminName', models.CharField(max_length=255)),
                ('AdminEmail', models.CharField(max_length=255)),
                ('AdminPassword', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Admin_Drop_Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DropName', models.CharField(max_length=255)),
                ('DropNum', models.IntegerField(default=0)),
                ('DateTime', models.DateField(default=datetime.date(2024, 3, 11))),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('zipcode', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('size', models.CharField(max_length=255)),
                ('totalprice', models.FloatField()),
                ('payment_id', models.CharField(max_length=255, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out for shipping', 'Out for shipping'), ('Completed', 'Completed')], default='Pending', max_length=255)),
                ('message', models.TextField(null=True)),
                ('trackingno', models.CharField(max_length=255, null=True)),
                ('trackinglink', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(max_length=255)),
                ('Catgories', models.CharField(choices=[('Top', 'Top'), ('Crop Top', 'Crop Top'), ('Crop Shirt', 'Crop Shirt'), ('Shirt', 'Shirt'), ('Tshirt', 'Tshirt'), ('Crop Tshirt', 'Crop Tshirt'), ('Tank', 'Tank'), ('Chiffon Top', 'Chiffon Top'), ('Dress', 'Dress'), ('Sweater', 'Sweater'), ('Cardigan', 'Cardigan'), ('Hoodie', 'Hoodie'), ('SweatShirt', 'SweatShirt'), ('Pre Winter', 'Pre Winter'), ('Denim Jacket', 'Denim Jacket'), ('Puffer Jacket', 'Puffer Jacket'), ('Trench Coat', 'Trench Coat'), ('Hoodie', 'Hoodie'), ('Shacket', 'Shacket'), ('Jeans', 'Jeans'), ('Trouser', 'Trouser'), ('Cargo', 'Cargo'), ('Shorts', 'Shorts'), ('Skirt', 'Skirt')], max_length=255)),
                ('Price', models.IntegerField()),
                ('TypeOfStock', models.CharField(choices=[('Special', 'Special'), ('Sale', 'Sale'), ('Drop', 'Drop'), ('General', 'General')], max_length=255)),
                ('BustOrWaist', models.CharField(max_length=255)),
                ('Condition', models.IntegerField()),
                ('Details', models.TextField()),
                ('Image1', models.ImageField(blank=True, upload_to='media/pics')),
                ('Image2', models.ImageField(blank=True, upload_to='media/pics')),
                ('Image3', models.ImageField(blank=True, upload_to='media/pics')),
                ('Image4', models.ImageField(blank=True, upload_to='media/pics')),
                ('Image5', models.ImageField(blank=True, upload_to='media/pics')),
                ('FreeSize', models.IntegerField(default=0)),
                ('Size22', models.IntegerField(default=0)),
                ('Size23', models.IntegerField(default=0)),
                ('Size24', models.IntegerField(default=0)),
                ('Size25', models.IntegerField(default=0)),
                ('Size26', models.IntegerField(default=0)),
                ('Size27', models.IntegerField(default=0)),
                ('Size28', models.IntegerField(default=0)),
                ('Size29', models.IntegerField(default=0)),
                ('Size30', models.IntegerField(default=0)),
                ('Size31', models.IntegerField(default=0)),
                ('Size32', models.IntegerField(default=0)),
                ('Size33', models.IntegerField(default=0)),
                ('Size34', models.IntegerField(default=0)),
                ('Size35', models.IntegerField(default=0)),
                ('Size36', models.IntegerField(default=0)),
                ('Size37', models.IntegerField(default=0)),
                ('Size38', models.IntegerField(default=0)),
                ('Size39', models.IntegerField(default=0)),
                ('Size40', models.IntegerField(default=0)),
                ('Size41', models.IntegerField(default=0)),
                ('Size42', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=255)),
                ('MobileNo', models.IntegerField()),
                ('Emailid', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=255)),
                ('ConfirmPassword', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TrackingDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trackingno', models.CharField(max_length=255, null=True)),
                ('trackinglink', models.CharField(max_length=255, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NithClothingApp.order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NithClothingApp.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NithClothingApp.products')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NithClothingApp.user'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productsize', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NithClothingApp.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NithClothingApp.user')),
            ],
        ),
    ]
