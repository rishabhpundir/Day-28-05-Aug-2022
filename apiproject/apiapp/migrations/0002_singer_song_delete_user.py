# Generated by Django 4.0.6 on 2022-08-05 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('gender', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('singer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sungby', to='apiapp.singer')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
