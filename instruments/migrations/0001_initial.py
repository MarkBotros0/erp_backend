# Generated by Django 3.2.25 on 2024-08-06 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bond',
            fields=[
                ('bond_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('abbreviation', models.CharField(blank=True, max_length=20)),
                ('issue_date', models.DateField()),
                ('subscription_close_date', models.DateField()),
                ('maturity_date', models.DateField()),
                ('currency', models.CharField(max_length=3)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quota', models.PositiveIntegerField()),
                ('is_bookkeeping', models.BooleanField(default=False)),
                ('bookkeeping_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BondType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CallAccount',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=15)),
                ('currency', models.CharField(max_length=3)),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('last_interest_calculation_date', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_management.client')),
            ],
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('currency', models.CharField(max_length=3)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('is_auto_renewable', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('MATURED', 'Matured'), ('LIQUIDATED', 'Liquidated')], max_length=20)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_management.client')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('fund_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('inception_date', models.DateField()),
                ('nav', models.DecimalField(decimal_places=2, max_digits=15)),
                ('currency', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='FundType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Premium',
            fields=[
                ('premium_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('abbreviation', models.CharField(blank=True, max_length=20)),
                ('foreign_name', models.CharField(blank=True, max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('number_of_shares', models.IntegerField(blank=True, null=True)),
                ('country', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('egypt_value', models.IntegerField(blank=True, null=True)),
                ('sector', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='instruments.sector')),
            ],
        ),
        migrations.CreateModel(
            name='StockExchange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TreasuryBill',
            fields=[
                ('tbill_id', models.AutoField(primary_key=True, serialize=False)),
                ('issue_date', models.DateField()),
                ('maturity_date', models.DateField()),
                ('face_value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('discount_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('currency', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='TreasuryBillTrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_date', models.DateTimeField()),
                ('trade_type', models.CharField(choices=[('BUY', 'Buy'), ('SELL', 'Sell')], max_length=4)),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tbill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trades', to='instruments.treasurybill')),
            ],
        ),
        migrations.CreateModel(
            name='SubSector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instruments.sector')),
            ],
        ),
        migrations.CreateModel(
            name='StockTrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('trade_date', models.DateTimeField()),
                ('trade_type', models.CharField(choices=[('buy', 'Buy'), ('sell', 'Sell')], max_length=4)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_management.portfolio')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trades', to='instruments.stock')),
            ],
        ),
        migrations.CreateModel(
            name='StockIssue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateField()),
                ('currency', models.CharField(choices=[('EGP', 'EGP'), ('USD', 'USD'), ('SAR', 'SAR')], max_length=3)),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('coupon', models.IntegerField(blank=True, null=True)),
                ('is_internal', models.BooleanField(default=False)),
                ('is_listed', models.BooleanField(default=False)),
                ('book_keeping', models.BooleanField(default=False)),
                ('bk_date', models.DateField()),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='instruments.stock')),
            ],
        ),
        migrations.AddField(
            model_name='stock',
            name='stock_exchange',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='instruments.stockexchange'),
        ),
        migrations.AddField(
            model_name='stock',
            name='sub_sector',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='instruments.subsector'),
        ),
        migrations.CreateModel(
            name='PremiumTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateTimeField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_management.client')),
                ('premium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='instruments.premium')),
            ],
        ),
        migrations.CreateModel(
            name='FundTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateTimeField()),
                ('transaction_type', models.CharField(choices=[('SUBSCRIPTION', 'Subscription'), ('REDEMPTION', 'Redemption')], max_length=15)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('units', models.DecimalField(decimal_places=4, max_digits=15)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_management.client')),
                ('fund', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='instruments.fund')),
            ],
        ),
        migrations.CreateModel(
            name='FundDividend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('declaration_date', models.DateField()),
                ('ex_date', models.DateField()),
                ('payment_date', models.DateField()),
                ('amount_per_unit', models.DecimalField(decimal_places=4, max_digits=10)),
                ('fund', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dividends', to='instruments.fund')),
            ],
        ),
        migrations.AddField(
            model_name='fund',
            name='fund_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='instruments.fundtype'),
        ),
        migrations.CreateModel(
            name='DepositTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateTimeField()),
                ('transaction_type', models.CharField(choices=[('ISSUE', 'Issue'), ('SETTLE', 'Settle'), ('DECREASE', 'Decrease'), ('LIQUIDATE', 'Liquidate'), ('RENEW', 'Renew')], max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('deposit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='instruments.deposit')),
            ],
        ),
        migrations.CreateModel(
            name='CallAccountTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateTimeField()),
                ('transaction_type', models.CharField(choices=[('DEPOSIT', 'Deposit'), ('WITHDRAWAL', 'Withdrawal'), ('INTEREST', 'Interest')], max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='instruments.callaccount')),
            ],
        ),
        migrations.CreateModel(
            name='BondTrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_date', models.DateTimeField()),
                ('trade_type', models.CharField(choices=[('buy', 'Buy'), ('sell', 'Sell')], max_length=4)),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bond', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trades', to='instruments.bond')),
            ],
        ),
        migrations.CreateModel(
            name='BondCoupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_date', models.DateField()),
                ('coupon_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('is_paid', models.BooleanField(default=False)),
                ('bond', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coupons', to='instruments.bond')),
            ],
        ),
        migrations.AddField(
            model_name='bond',
            name='bond_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='instruments.bondtype'),
        ),
    ]
