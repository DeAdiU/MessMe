# Generated by Django 4.2.2 on 2023-06-30 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_record_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='username',
        ),
    ]
