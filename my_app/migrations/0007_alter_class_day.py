# Generated by Django 5.0.6 on 2024-07-06 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_class_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='day',
            field=models.CharField(default='一', max_length=1),
        ),
    ]
