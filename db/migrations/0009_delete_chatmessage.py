# Generated by Django 5.0.6 on 2025-03-21 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0008_remove_chatmessage_timestamp_chatmessage_created_at_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ChatMessage',
        ),
    ]
