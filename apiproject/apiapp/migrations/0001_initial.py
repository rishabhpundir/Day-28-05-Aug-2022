# Generated by Django 4.0.6 on 2022-08-05 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('age', models.IntegerField()),
                ('city', models.TextField(max_length=100)),
            ],
        ),
    ]