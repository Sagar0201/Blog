# Generated by Django 4.1.4 on 2022-12-17 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_complate_profile',
            field=models.BooleanField(default=False),
        ),
    ]