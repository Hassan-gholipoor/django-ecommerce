# Generated by Django 3.0.5 on 2022-06-05 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_decription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='decription',
            new_name='decsription',
        ),
    ]