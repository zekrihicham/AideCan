# Generated by Django 2.1.5 on 2019-03-30 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection_donnees', '0007_auto_20190330_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='phone_establishment',
        ),
    ]
