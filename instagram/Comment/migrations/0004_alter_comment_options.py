# Generated by Django 4.0.6 on 2022-08-16 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Comment', '0003_alter_comment_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_date']},
        ),
    ]