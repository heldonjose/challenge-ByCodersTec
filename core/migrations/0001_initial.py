# Generated by Django 3.2.7 on 2021-09-16 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('date_modificado', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=120)),
                ('document', models.CharField(max_length=14)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TransactionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('date_modificado', models.DateTimeField(auto_now=True, null=True)),
                ('cod', models.IntegerField()),
                ('description', models.CharField(max_length=255)),
                ('operation', models.CharField(choices=[('ENTRADA', '+'), ('SAIDA', '-')], max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TransactionStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('date_modificado', models.DateTimeField(auto_now=True, null=True)),
                ('date', models.DateTimeField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('documentRecipient', models.CharField(max_length=18)),
                ('numberCard', models.IntegerField()),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.store')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.transactiontype')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
