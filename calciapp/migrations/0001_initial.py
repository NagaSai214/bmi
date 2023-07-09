# Generated by Django 4.2.3 on 2023-07-07 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bmi_Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('height', models.FloatField(max_length=10)),
                ('weight', models.FloatField(max_length=10)),
                ('ph_no', models.CharField(max_length=30)),
                ('bmi_index', models.FloatField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Bmi_Users',
                'unique_together': {('ph_no',)},
            },
        ),
    ]