# Generated by Django 3.0.6 on 2020-05-25 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0004_auto_20200524_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
