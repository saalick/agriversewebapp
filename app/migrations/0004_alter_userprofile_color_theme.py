# Generated by Django 3.2.19 on 2023-05-31 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_userprofile_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='color_theme',
            field=models.CharField(choices=[('Dark', 'Dark'), ('Light', 'Light'), ('System Color', 'System Color')], default='Ligth', max_length=50),
        ),
    ]
