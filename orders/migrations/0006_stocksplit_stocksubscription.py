# Generated by Django 3.2.25 on 2024-08-28 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instruments', '0001_initial'),
        ('client_management', '0001_initial'),
        ('orders', '0005_cashdividendopeningbalance_stockdividenddiscounted'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('installment', models.BooleanField(default=False)),
                ('quantity', models.PositiveIntegerField()),
                ('subscription_type', models.CharField(choices=[('General', 'GENERAL'), ('Closed', 'CLOSED')], default='General', max_length=10)),
                ('qty_for_persons_min', models.PositiveIntegerField(blank=True, null=True)),
                ('qty_for_persons_max', models.PositiveIntegerField(blank=True, null=True)),
                ('qty_for_companies_min', models.PositiveIntegerField(blank=True, null=True)),
                ('qty_for_companies_max', models.PositiveIntegerField(blank=True, null=True)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_management.bank')),
                ('bank_branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_management.bankbranch')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instruments.stock')),
            ],
        ),
        migrations.CreateModel(
            name='StockSplit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('split_date', models.DateField()),
                ('ratio', models.DecimalField(decimal_places=4, max_digits=10)),
                ('notes', models.TextField(blank=True, null=True)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_management.bank')),
                ('bank_branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_management.bankbranch')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instruments.stock')),
            ],
        ),
    ]
