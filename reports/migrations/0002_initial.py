# Generated by Django 4.1.4 on 2022-12-18 04:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reports', '0001_initial'),
        ('tasks', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='runner_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='report',
            name='task_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.task'),
        ),
        migrations.AddField(
            model_name='report',
            name='visible_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.visibility'),
        ),
        migrations.AddField(
            model_name='imageloader',
            name='report_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.report'),
        ),
    ]