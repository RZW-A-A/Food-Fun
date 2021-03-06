# Generated by Django 3.1.1 on 2020-10-29 06:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('foodid', models.AutoField(primary_key=True, serialize=False)),
                ('foodname', models.CharField(max_length=50)),
                ('foodcategory', models.CharField(choices=[('starters', 'STARTERS'), ('maindish', 'MAINDISH'), ('deserts', 'DESERTS'), ('drinks', 'DRINKS')], default='maindish', max_length=20)),
                ('foodprice', models.FloatField()),
                ('foodimage', models.ImageField(blank=True, default='', null=True, upload_to='media')),
                ('fooddiscription', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('mobile', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('proficpic', models.ImageField(blank=True, default='/static/images/de.png', null=True, upload_to='profile')),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
