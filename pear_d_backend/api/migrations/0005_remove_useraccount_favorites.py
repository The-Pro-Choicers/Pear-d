# Generated by Django 4.1.3 on 2022-11-24 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_useraccount_prefer_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='favorites',
        ),
    ]