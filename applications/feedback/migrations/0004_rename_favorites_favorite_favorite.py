# Generated by Django 4.1.4 on 2022-12-17 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_alter_review_owner_favorite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favorite',
            old_name='favorites',
            new_name='favorite',
        ),
    ]
