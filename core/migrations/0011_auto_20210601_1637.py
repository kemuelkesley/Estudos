# Generated by Django 3.2.3 on 2021-06-01 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20210601_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastrocliente',
            name='bairro',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='cadastrocliente',
            name='cidade',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='cadastrocliente',
            name='endereco',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='cadastrocliente',
            name='profissao',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Profissão'),
        ),
    ]
