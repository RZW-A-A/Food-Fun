# Generated by Django 3.1.1 on 2020-11-03 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0003_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=20)),
                ('mobile', models.CharField(max_length=10)),
            ],
        ),
    ]