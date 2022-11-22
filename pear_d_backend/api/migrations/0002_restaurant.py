# Generated by Django 4.1.3 on 2022-11-21 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('address', models.CharField(max_length=128, unique=True)),
                ('photo_ref', models.CharField(max_length=128, unique=True)),
                ('price_level', models.IntegerField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('url', models.CharField(max_length=128, unique=True)),
                ('env_conscious', models.BooleanField(default=False)),
                ('minority', models.BooleanField(default=False)),
                ('philanthropic', models.BooleanField(default=False)),
            ],
        ),
    ]
