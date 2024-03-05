# Generated by Django 4.2.10 on 2024-03-05 08:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('view_log', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewlog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='view_logs', to=settings.AUTH_USER_MODEL),
        ),
    ]