# Generated by Django 3.2.8 on 2021-10-12 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email_id', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('user_name', models.CharField(max_length=30)),
            ],
        ),
    ]
