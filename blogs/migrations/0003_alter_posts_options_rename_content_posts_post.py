# Generated by Django 4.2.7 on 2023-11-13 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_posts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'verbose_name_plural': 'posts'},
        ),
        migrations.RenameField(
            model_name='posts',
            old_name='content',
            new_name='post',
        ),
    ]