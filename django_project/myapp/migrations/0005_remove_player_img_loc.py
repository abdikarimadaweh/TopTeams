# Generated by Django 3.2.9 on 2021-12-03 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_player_img_loc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='img_loc',
        ),
    ]