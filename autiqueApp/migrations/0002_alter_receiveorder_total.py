# Generated by Django 5.0.2 on 2024-03-13 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autiqueApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiveorder',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
    ]