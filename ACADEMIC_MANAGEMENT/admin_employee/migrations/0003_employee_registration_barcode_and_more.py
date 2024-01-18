# Generated by Django 4.2.7 on 2024-01-16 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_employee', '0002_remove_employee_registration_barcode_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_registration',
            name='Barcode',
            field=models.ImageField(blank=True, null=True, upload_to='barcode/'),
        ),
        migrations.AddField(
            model_name='employee_registration',
            name='Photo',
            field=models.ImageField(blank=True, null=True, upload_to='employee_photos/'),
        ),
    ]
