# Generated by Django 4.2.1 on 2023-05-16 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_contact_username_contact_name1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='about',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='name1',
        ),
    ]
