# Generated by Django 3.2.12 on 2024-01-23 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pilgrimage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pilgrim',
            name='service',
            field=models.CharField(choices=[('Suprabatha', 'Suprabatha'), ('Angapradakshina', 'Angapradakshina'), ('Thomala', 'Thomala'), ('Kalyanam', 'Kalyanam'), ('Bramhotsavam', 'Bramhotsavam')], default='Suprabatha', max_length=15),
        ),
    ]
