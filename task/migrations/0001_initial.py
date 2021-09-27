# Generated by Django 3.2.5 on 2021-09-21 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conversion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_currency_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='From Code')),
                ('to_currency_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='To Code')),
                ('from_currency_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='From name')),
                ('to_currency_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='To Name')),
                ('exchange_rate', models.DecimalField(decimal_places=8, max_digits=15, verbose_name='Exchange Rate')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='Updated At')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
            ],
            options={
                'verbose_name': 'Conversion',
                'verbose_name_plural': 'Conversion',
            },
        ),
    ]