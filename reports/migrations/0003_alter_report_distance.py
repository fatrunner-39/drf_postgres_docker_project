# Generated by Django 4.1.4 on 2022-12-18 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='distance',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True),
        ),
    ]
