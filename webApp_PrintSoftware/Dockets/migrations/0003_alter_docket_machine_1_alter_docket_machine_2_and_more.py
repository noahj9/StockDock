# Generated by Django 4.0.6 on 2023-02-14 00:19

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Dockets', '0002_alter_docket_machine_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docket',
            name='machine_1',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Xerox 1000', 'Xerox 1000'), ('Xerox Nuvera', 'Xerox Nuvera')], max_length=100),
        ),
        migrations.AlterField(
            model_name='docket',
            name='machine_2',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Xerox 1000', 'Xerox 1000'), ('Xerox Nuvera', 'Xerox Nuvera')], max_length=100),
        ),
        migrations.AlterField(
            model_name='docket',
            name='machine_3',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Xerox 1000', 'Xerox 1000'), ('Xerox Nuvera', 'Xerox Nuvera')], max_length=100),
        ),
    ]
