# Generated by Django 3.2.4 on 2021-06-27 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserCredential',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=25)),
                ('role', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
