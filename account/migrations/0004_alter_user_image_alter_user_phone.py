# Generated by Django 4.0.6 on 2022-08-15 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='phone number'),
        ),
    ]
