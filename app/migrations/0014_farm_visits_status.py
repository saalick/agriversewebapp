# Generated by Django 3.2.19 on 2023-07-02 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_farm_number_of_trees'),
    ]

    operations = [
        migrations.AddField(
            model_name='farm',
            name='Visits_Status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Booked', 'Booked'), ('Reject', 'Reject'), ('Completed', 'Completed')], default='Pending', max_length=50),
        ),
    ]