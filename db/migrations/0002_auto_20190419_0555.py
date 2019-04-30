# Generated by Django 2.0.7 on 2019-04-19 05:55

from django.db import migrations, models
import shortuuid.main


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='id',
            field=models.CharField(default=shortuuid.main.ShortUUID.random, max_length=12, primary_key=True, serialize=False),
        ),
    ]