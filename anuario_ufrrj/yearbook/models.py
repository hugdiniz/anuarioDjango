from django.db import models

# Create your models here.

class Funcao(models.Model):
	nome = models.CharField(max_length=200)

class Lotacao(models.Model):
	nome = models.CharField(max_length=200)
	funcao = models.ForeignKey(Funcao)

class Unidade_Organizacional(models.Model):
    nome = models.CharField(max_length=200)
    abreviacao = models.CharField(max_length=200, blank=True)
    unidade_org = models.ForeignKey('self')

class Sala(models.Model):
    identificador = models.CharField(max_length=200)
    unidade = models.ForeignKey(Unidade_Organizacional)

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    nascimento = models.DateTimeField('data de nascimento')
    foto = models.CharField(max_length=200, blank=True)
    lotacao_atual = models.ForeignKey(Lotacao)
    historico = models.ManyToManyField(Lotacao, related_name='lotacoes_anteriores')

class Cargo(models.Model):
    nome = models.CharField(max_length=200)
    oucupante = models.ForeignKey(Pessoa)

