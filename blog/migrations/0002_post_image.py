# Generated by Django 3.2.9 on 2021-11-28 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=1, upload_to='static/', verbose_name='Post Image:'),
            preserve_default=False,
        ),
    ]