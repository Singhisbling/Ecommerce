# Generated by Django 2.0.6 on 2018-07-12 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Eco', '0020_order_current_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='order',
        ),
        migrations.RemoveField(
            model_name='order',
            name='current_address',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Eco.Address'),
        ),
    ]
