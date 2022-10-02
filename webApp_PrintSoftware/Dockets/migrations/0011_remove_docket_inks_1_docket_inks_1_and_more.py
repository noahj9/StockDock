# Generated by Django 4.0.6 on 2022-10-02 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dockets', '0010_remove_docket_stock_1_docket_stock_1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docket',
            name='inks_1',
        ),
        migrations.AddField(
            model_name='docket',
            name='inks_1',
            field=models.ManyToManyField(to='Dockets.ink'),
        ),
        migrations.RemoveField(
            model_name='docket',
            name='proof_1',
        ),
        migrations.AddField(
            model_name='docket',
            name='proof_1',
            field=models.ManyToManyField(to='Dockets.proof'),
        ),
    ]