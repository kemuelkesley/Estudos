from django.db import models
from django.db.models import indexes
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, PROTECT
from django.db.models.fields import BigAutoField
from django.utils import timezone





# Cadastro de Cidade.


class Cidade(models.Model):
    nome = models.CharField(max_length=30, blank=True, null=True, verbose_name='Nome da Cidade')
    def __str__(self):
        return self.nome 


# Cadastro do Bairro


class Bairro(models.Model):
    nome = models.CharField(max_length=60, blank=True, null=True, verbose_name='Nome do Bairro')
    def __str__(self):
        return self.nome




# Cadastro de Evento

class Evento(models.Model):
    nome_evento = models.CharField(max_length=100, verbose_name='Nome do Evento')
    slug = models.CharField(max_length=100, blank=True, null=True,verbose_name='Slug')
    data_evento = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')
    Cidade = models.ForeignKey(Cidade, blank=True, null=True, on_delete=models.PROTECT)
    Bairro = models.ForeignKey(Bairro, blank=True, null=True, on_delete=models.PROTECT)    
        
    def __str__ (self):
        return self.nome_evento


# Escolha de Sexo do Cliente.


class Sexo(models.Model):
    sexo = models.CharField(max_length=20)  

    class Meta:
        verbose_name_plural='Sexo'

    def __str__(self):
        return self.sexo



# Cadastro de Clientes
    
class CadastroCliente(models.Model):      
        
    nome_completo = models.CharField(max_length=100, verbose_name='Nome Completo')
    Sexo = models.ForeignKey(Sexo, blank=True, null=True, on_delete=models.PROTECT)
    data_nascimento = models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')
    rg = models.CharField(max_length=13, verbose_name='RG')
    cpf = models.CharField(default='CPF sem espaços', max_length=11, verbose_name='CPF')
    cidade = models.CharField(max_length=100, blank=True, null=True, verbose_name='Cidade')
    bairro = models.CharField(max_length=100, blank=True, null=True, verbose_name='Bairro')
    endereco = models.CharField(max_length=100, default='Rua', blank=True, null=True, verbose_name='Endereço')
    numero = models.IntegerField(default=0)
    cep = models.CharField(max_length=8, blank=True, null=True, verbose_name='CEP')
    profissao = models.CharField(max_length=100, blank=True, null=True, verbose_name='Profissão')
    email = models.EmailField(default='Digite seu E-mail', verbose_name='E-mail')
    contato = models.CharField(max_length=14, blank=True, null=True, verbose_name='Celular', default='(082)')

    class Meta:
        verbose_name_plural='Cadastros'

    def __str__ (self):
        return self.nome_completo

