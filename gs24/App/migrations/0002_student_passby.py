# Generated by Django 4.2.3 on 2023-08-02 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='passby',
            field=models.CharField(default='', max_length=100),
        ),
    ]