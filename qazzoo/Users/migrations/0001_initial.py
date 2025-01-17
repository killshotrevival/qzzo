# Generated by Django 3.0.5 on 2020-08-24 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('artist_photo', models.ImageField(default='ap_default.jpg', upload_to='artist_photo')),
                ('cover_photo', models.ImageField(default='cp_default.jpg', upload_to='cover_photo')),
                ('place', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=2000)),
                ('badge', models.CharField(max_length=20)),
                ('fb', models.CharField(default='facebook.com', max_length=100)),
                ('insta', models.CharField(default='instagram.com', max_length=100)),
            ],
        ),
    ]
