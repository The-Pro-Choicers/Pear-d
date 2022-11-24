# Generated by Django 4.1.3 on 2022-11-24 07:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_useraccount_favorites'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_id', models.IntegerField(default=0)),
                ('num_chosen', models.IntegerField(default=0)),
                ('user_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
