# Generated by Django 4.1.4 on 2022-12-16 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Material',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='material',
        ),
    ]
