# Generated by Django 5.0.6 on 2024-07-06 14:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0006_rename_filetype_attachmenttype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='file_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachment_type', to='materials.attachmenttype', verbose_name='Тип файла'),
        ),
    ]