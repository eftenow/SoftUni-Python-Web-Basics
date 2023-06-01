from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name=30)),
                ('personal_photo', models.URLField()),
                ('date_of_brith', models.DateField(blank=True, null=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
