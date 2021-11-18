# Generated by Django 3.2.7 on 2021-10-07 23:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adoptLifeApp', '0005_testimonial_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='pqrs',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='my_pqrs', to=settings.AUTH_USER_MODEL),
        ),
    ]
