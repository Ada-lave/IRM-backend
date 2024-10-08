# Generated by Django 5.0.6 on 2024-09-19 00:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0013_attachment_section_alter_attachment_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='materials.section', verbose_name='К какому разделу сайта'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='theme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='materials.theme', verbose_name='К какому материалу'),
        ),
        migrations.AlterField(
            model_name='section',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на раздел'),
        ),
    ]
