# Generated by Django 5.0.1 on 2024-03-06 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_note_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
    ]
