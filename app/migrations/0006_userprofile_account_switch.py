# Generated by Django 3.2.19 on 2023-05-31 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_userprofile_color_theme'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='Account_switch',
            field=models.CharField(choices=[('Enable', 'Enable'), ('Disable', 'Disable')], default='Enable', max_length=50),
        ),
    ]
