# Generated by Django 2.0.7 on 2018-07-11 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Eco', '0016_auto_20180711_0615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Eco.Address'),
        ),
        migrations.AlterField(
            model_name='address',
            name='current_address',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
