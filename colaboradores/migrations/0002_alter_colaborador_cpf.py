# Generated by Django 3.2.9 on 2021-11-18 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colaboradores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='cpf',
            field=models.CharField(max_length=11, null=True, unique=True),
        ),
    ]