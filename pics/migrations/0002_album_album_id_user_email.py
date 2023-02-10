# Generated by Django 4.1.6 on 2023-02-10 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='STRING', max_length=300),
        ),
    ]