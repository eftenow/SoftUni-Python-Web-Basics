# Generated by Django 4.2.1 on 2023-06-26 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0006_alter_photo_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photolike',
            name='to_photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='photos.photo'),
        ),
        migrations.AlterField(
            model_name='photolike',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
