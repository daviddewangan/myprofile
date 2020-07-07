# Generated by Django 2.2.10 on 2020-07-05 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0006_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('exp', models.CharField(choices=[('beginer', 'beg'), ('intermediate', 'inter'), ('professional', 'pro')], max_length=200)),
                ('percent', models.IntegerField()),
            ],
        ),
    ]
