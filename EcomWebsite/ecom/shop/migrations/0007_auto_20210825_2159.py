# Generated by Django 3.2.6 on 2021-08-25 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20210825_2000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address2',
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='order',
            name='zip_code',
            field=models.CharField(max_length=10),
        ),
    ]
