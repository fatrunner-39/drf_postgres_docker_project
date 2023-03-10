# Generated by Django 4.1.4 on 2022-12-19 12:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reports', '0004_alter_imageloader_report_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_date', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(max_length=1000)),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comments.comment')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
                ('report_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.report')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='getter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
