# Generated by Django 4.2.7 on 2024-01-03 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_general', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emp_category',
            old_name='Designation_Area',
            new_name='Employee_Area',
        ),
        migrations.RenameField(
            model_name='emp_category',
            old_name='Emp_category_Name',
            new_name='Employee_Name',
        ),
    ]
