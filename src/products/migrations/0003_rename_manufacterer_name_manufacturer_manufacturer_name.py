# Generated by Django 5.1.4 on 2024-12-19 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manufacturer',
            old_name='manufacterer_name',
            new_name='manufacturer_name',
        ),
    ]
