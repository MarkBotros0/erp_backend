# Generated by Django 3.2.25 on 2024-08-06 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='price_deal',
            new_name='deal_price',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='executed_qty',
            new_name='executed_quantity',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='price_marketing',
            new_name='marketing_price',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='date_order',
            new_name='order_date',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='value_order',
            new_name='order_value',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='factor_safety',
            new_name='safety_factor',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='day_same',
            new_name='same_day',
        ),
        migrations.RemoveField(
            model_name='order',
            name='margin_is',
        ),
        migrations.AddField(
            model_name='order',
            name='is_margin',
            field=models.BooleanField(default=False, verbose_name='Is margin'),
        ),
    ]
