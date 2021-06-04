# Generated by Django 3.2.3 on 2021-06-04 18:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_evento_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='slug',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='cadastrocliente',
            name='contato',
            field=models.CharField(blank=True, default='(082)', max_length=14, null=True, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='cadastrocliente',
            name='cpf',
            field=models.CharField(default='CPF sem espaços', max_length=11, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='cadastrocliente',
            name='email',
            field=models.EmailField(default='Digite seu E-mail', max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='cadastrocliente',
            name='endereco',
            field=models.CharField(blank=True, default='Rua', max_length=100, null=True, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='data_evento',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]