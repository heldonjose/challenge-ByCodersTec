# Generated by Django 3.2.7 on 2021-09-16 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_rename_importcnad_importcnab'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='document',
            field=models.CharField(max_length=18, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='transactiontype',
            name='cod',
            field=models.IntegerField(unique=True),
        ),
    ]