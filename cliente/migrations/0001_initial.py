# Generated by Django 4.0.5 on 2022-06-30 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=80)),
                ('whatsapp', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Cliente',
            },
        ),
    ]
