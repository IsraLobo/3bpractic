# Generated by Django 4.2.13 on 2024-06-25 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('approject3b', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='id_user',
            field=models.IntegerField(blank=True, null=True, verbose_name='Id Usuario'),
        ),
        migrations.AddField(
            model_name='products',
            name='user_save',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Usuario que Guardo'),
        ),
    ]
