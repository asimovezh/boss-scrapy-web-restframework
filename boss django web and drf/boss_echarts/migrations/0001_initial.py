# Generated by Django 2.0.7 on 2018-11-16 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boss',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('job_name', models.CharField(blank=True, max_length=100, null=True)),
                ('salary', models.CharField(blank=True, max_length=100, null=True)),
                ('area', models.CharField(blank=True, max_length=100, null=True)),
                ('experience', models.CharField(blank=True, max_length=100, null=True)),
                ('education', models.CharField(blank=True, max_length=100, null=True)),
                ('industry', models.CharField(blank=True, max_length=100, null=True)),
                ('listed_info', models.CharField(blank=True, max_length=100, null=True)),
                ('employee_num', models.CharField(blank=True, max_length=100, null=True)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('pub_date', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'boss',
                'managed': True,
            },
        ),
    ]
