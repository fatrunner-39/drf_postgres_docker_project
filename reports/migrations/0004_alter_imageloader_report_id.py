# Generated by Django 4.1.4 on 2022-12-19 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_alter_report_distance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageloader',
            name='report_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='reports.report'),
        ),
    ]
