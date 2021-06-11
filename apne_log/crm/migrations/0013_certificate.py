# Generated by Django 3.2.4 on 2021-06-10 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crm', '0012_delete_certificate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=245)),
                ('type', models.CharField(choices=[('Student', 'Student'), ('Individual', 'Individual')], max_length=245)),
                ('college', models.CharField(max_length=245)),
                ('dept_name', models.CharField(max_length=245)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
    ]
