# Generated by Django 2.1.7 on 2019-03-06 18:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]