# Generated by Django 4.2.1 on 2023-06-26 07:59

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import petstagram.accounts.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), petstagram.accounts.validators.name_contains_only_letters])),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), petstagram.accounts.validators.name_contains_only_letters])),
                ('profile_picture', models.URLField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Do not show', 'Do not show')])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]