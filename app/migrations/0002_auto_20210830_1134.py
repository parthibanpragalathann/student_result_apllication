# Generated by Django 3.2.6 on 2021-08-30 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_details',
            name='results',
        ),
        migrations.AlterField(
            model_name='student_details',
            name='marks',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
