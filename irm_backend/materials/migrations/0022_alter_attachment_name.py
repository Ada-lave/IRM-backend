# Generated by Django 5.0.6 on 2024-12-29 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0021_alter_section_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='name',
            field=models.CharField(max_length=512, verbose_name='Имя файла'),
        ),
    ]
