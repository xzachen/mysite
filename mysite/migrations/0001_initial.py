# Generated by Django 2.0.1 on 2018-04-11 06:51

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'user',
                'ordering': ['userid'],
            },
            managers=[
                ('maneger', django.db.models.manager.Manager()),
            ],
        ),
    ]
