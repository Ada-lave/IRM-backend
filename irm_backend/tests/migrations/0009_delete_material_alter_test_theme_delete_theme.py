# Generated by Django 5.0.6 on 2024-05-29 08:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
        ('tests', '0008_rename_meterial_material_alter_answer_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Material',
        ),
        migrations.AlterField(
            model_name='test',
            name='theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materials.theme', verbose_name='Тема'),
        ),
        migrations.DeleteModel(
            name='Theme',
        ),
    ]
