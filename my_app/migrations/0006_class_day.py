# Generated by Django 5.0.6 on 2024-07-06 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_alter_class_tid_alter_enrolled_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='day',
            field=models.IntegerField(default=1),
        ),
    ]
