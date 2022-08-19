# Generated by Django 4.0.6 on 2022-07-20 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('N', 'Prefer Not To Say'), ('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures'),
        ),
    ]