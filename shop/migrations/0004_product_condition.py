# Generated by Django 3.2.15 on 2022-08-26 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('ss', 'بهار تابستان'), ('fw', 'پایزز زمستون'), ('di', 'تخفیف')], max_length=2, null=True, verbose_name='حالت'),
        ),
    ]
