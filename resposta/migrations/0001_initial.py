# Generated by Django 4.0.5 on 2022-06-30 00:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pesquisa', '0001_initial'),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resposta_cli', models.CharField(choices=[('Muito satisfeito', 'Muito satisfeito'), ('Satisfeito', 'Satisfeito'), ('Neutro', 'Neutro'), ('Insatisfeito', 'Insatisfeito'), ('Muito insatisfeito', 'Muito insatisfeito')], default='Neutro', max_length=20)),
                ('data_resposta', models.DateTimeField(default=datetime.date(2022, 6, 29))),
                ('item_pesquisa', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pesquisa.item_pesquisa')),
                ('nome_cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cliente.cliente')),
            ],
        ),
    ]
