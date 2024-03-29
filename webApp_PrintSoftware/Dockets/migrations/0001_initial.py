# Generated by Django 4.0.6 on 2022-11-30 21:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Dockets.client')),
            ],
        ),
        migrations.CreateModel(
            name='Csr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposit', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ink', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Terms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Rep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('csr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Dockets.csr')),
            ],
        ),
        migrations.CreateModel(
            name='Docket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('date_required', models.DateField()),
                ('flexibility', models.CharField(max_length=100)),
                ('customer_PO', models.CharField(max_length=100)),
                ('quote', models.CharField(max_length=100, null=True)),
                ('deposit_amount', models.CharField(blank=True, max_length=100, null=True)),
                ('reception_notes', models.TextField(blank=True)),
                ('quantity_1', models.CharField(max_length=100)),
                ('description_1', models.CharField(max_length=100)),
                ('finished_size_1', models.CharField(max_length=100)),
                ('stock_1', models.CharField(max_length=100)),
                ('machine_1', models.CharField(max_length=200)),
                ('run_quantity_1', models.CharField(max_length=100)),
                ('sheet_size_1', models.CharField(max_length=100)),
                ('run_size_1', models.CharField(max_length=100)),
                ('proof_1', models.CharField(max_length=100)),
                ('inks_1', models.CharField(max_length=100)),
                ('instructions_1', models.TextField(blank=True)),
                ('bindery_1', models.CharField(max_length=100)),
                ('file_1', models.CharField(max_length=100)),
                ('price_comission_1', models.CharField(max_length=100)),
                ('shipping_1', models.CharField(max_length=100)),
                ('quantity_2', models.CharField(blank=True, max_length=100)),
                ('description_2', models.CharField(blank=True, max_length=100)),
                ('finished_size_2', models.CharField(blank=True, max_length=100)),
                ('stock_2', models.CharField(blank=True, max_length=100, null=True)),
                ('machine_2', models.CharField(blank=True, max_length=200)),
                ('run_quantity_2', models.CharField(blank=True, max_length=100)),
                ('sheet_size_2', models.CharField(blank=True, max_length=100)),
                ('run_size_2', models.CharField(blank=True, max_length=100)),
                ('proof_2', models.CharField(blank=True, max_length=100, null=True)),
                ('inks_2', models.CharField(blank=True, max_length=100, null=True)),
                ('instructions_2', models.TextField(blank=True)),
                ('bindery_2', models.CharField(blank=True, max_length=100)),
                ('file_2', models.CharField(blank=True, max_length=100)),
                ('price_comission_2', models.CharField(blank=True, max_length=100)),
                ('shipping_2', models.CharField(blank=True, max_length=100)),
                ('quantity_3', models.CharField(blank=True, max_length=100)),
                ('description_3', models.CharField(blank=True, max_length=100)),
                ('finished_size_3', models.CharField(blank=True, max_length=100)),
                ('stock_3', models.CharField(blank=True, max_length=100, null=True)),
                ('machine_3', models.CharField(blank=True, max_length=200)),
                ('run_quantity_3', models.CharField(blank=True, max_length=100)),
                ('sheet_size_3', models.CharField(blank=True, max_length=100)),
                ('run_size_3', models.CharField(blank=True, max_length=100)),
                ('proof_3', models.CharField(blank=True, max_length=100, null=True)),
                ('inks_3', models.CharField(blank=True, max_length=100, null=True)),
                ('instructions_3', models.TextField(blank=True)),
                ('bindery_3', models.CharField(blank=True, max_length=100)),
                ('file_3', models.CharField(blank=True, max_length=100)),
                ('price_comission_3', models.CharField(blank=True, max_length=100)),
                ('shipping_3', models.CharField(blank=True, max_length=100)),
                ('contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Dockets.contact')),
                ('csr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Dockets.csr')),
                ('customer_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Dockets.client')),
                ('deposit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Dockets.deposit')),
                ('rep', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Dockets.rep')),
                ('terms', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Dockets.terms')),
            ],
        ),
    ]
