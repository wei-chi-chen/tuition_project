# Generated by Django 5.0.6 on 2024-07-21 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0011_alter_enrolled_remark_alter_students_remark'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('catId', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(default='-', max_length=1000, null=True)),
            ],
            options={
                'db_table': 'Category',
            },
        ),
        migrations.AddField(
            model_name='teacher',
            name='line',
            field=models.CharField(default='-', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='phone',
            field=models.CharField(default='-', max_length=10, null=True),
        ),
    ]
