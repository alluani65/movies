# Generated by Django 5.0 on 2024-01-07 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default=1, upload_to='moviepics'),
            preserve_default=False,
        ),
    ]
