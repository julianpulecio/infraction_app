# Generated by Django 4.1.7 on 2023-02-19 20:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('infraction', '0004_rename_police_infraction_policeman'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infraction',
            name='policeman',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='infractions', to=settings.AUTH_USER_MODEL),
        ),
    ]