# Generated by Django 5.0.6 on 2024-07-06 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0005_alter_attachment_material'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FileType',
            new_name='AttachmentType',
        ),
    ]
