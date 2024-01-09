# Generated by Django 3.2.19 on 2023-06-22 17:54

from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_plot_booked_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='farm',
            name='Map',
            field=location_field.models.plain.PlainLocationField(blank=True, default='', max_length=63, null=True),
        ),
        migrations.AddField(
            model_name='farm',
            name='location',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
    ]
