# Generated by Django 5.1.2 on 2024-12-30 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_created_at_profile_updated_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-created_at', '-updated_at']},
        ),
    ]