# Generated by Django 4.2.8 on 2023-12-13 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='image',
            field=models.ImageField(null=True, upload_to='teams/images', verbose_name='Фото участника'),
        ),
    ]
