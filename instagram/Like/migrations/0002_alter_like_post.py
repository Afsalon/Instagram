# Generated by Django 4.0.6 on 2022-07-20 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_alter_post_updated_date'),
        ('Like', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Post.post'),
        ),
    ]