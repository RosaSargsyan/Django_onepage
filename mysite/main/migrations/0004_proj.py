# Generated by Django 4.2.1 on 2023-05-16 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_about_img_home_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name proj')),
                ('img', models.ImageField(upload_to='photo', verbose_name='About img')),
            ],
        ),
    ]