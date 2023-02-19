# Generated by Django 4.1.7 on 2023-02-19 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
        ('infraction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='infraction',
            name='police',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='infractions', to='person.person'),
            preserve_default=False,
        ),
    ]
