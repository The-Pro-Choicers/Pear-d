# Generated by Django 4.1.3 on 2022-11-23 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_restaurant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccount',
            old_name='is_dev',
            new_name='is_staff',
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
