# Generated by Django 3.2.4 on 2021-06-06 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20210606_1515'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='certificate_details',
            new_name='Certificate',
        ),
    ]