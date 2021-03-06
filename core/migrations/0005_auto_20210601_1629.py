# Generated by Django 3.2.3 on 2021-06-01 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_evento_cidade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=60, null=True, verbose_name='Nome do Bairro')),
            ],
        ),
        migrations.AddField(
            model_name='evento',
            name='Bairro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.bairro'),
        ),
    ]
