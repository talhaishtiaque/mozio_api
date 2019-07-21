# Generated by Django 2.2.3 on 2019-07-20 18:53

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(default='name@email.com', max_length=254)),
                ('phone_number', models.CharField(default='0000000', max_length=100)),
                ('language', models.CharField(default='English', max_length=50)),
                ('currency', models.CharField(default='USD', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Jeojson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default='1000', max_length=100)),
                ('jeojson', jsonfield.fields.JSONField(default='English', max_length=50)),
                ('provider_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mozio_providers.Provider')),
            ],
        ),
    ]