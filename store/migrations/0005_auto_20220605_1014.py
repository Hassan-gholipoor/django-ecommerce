# Generated by Django 3.0.5 on 2022-06-05 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20220605_1013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='decsription',
            new_name='description',
        ),
    ]
