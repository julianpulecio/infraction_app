# Generated by Django 4.1.7 on 2023-02-18 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policeman', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='policeman',
            name='identification_number',
            field=models.CharField(default=1, max_length=6, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='policeman',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='policeman',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]
