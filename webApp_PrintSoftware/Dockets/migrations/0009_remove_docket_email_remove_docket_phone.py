# Generated by Django 4.0.6 on 2022-10-02 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dockets', '0008_remove_docket_machine_1_docket_machine_1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docket',
            name='email',
        ),
        migrations.RemoveField(
            model_name='docket',
            name='phone',
        ),
    ]
