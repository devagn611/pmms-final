# Generated by Django 5.1.4 on 2025-01-10 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_skill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='owner',
        ),
    ]
