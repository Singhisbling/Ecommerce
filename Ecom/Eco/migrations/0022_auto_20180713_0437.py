# Generated by Django 2.0.7 on 2018-07-13 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Eco', '0021_auto_20180712_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='address', to='Eco.Address'),
        ),
    ]
