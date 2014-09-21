from django.db import models

# Create your models here.

class Funcao(models.Model):
	nome = models.CharField(max_length=200)

# class Lotacao(models.Model):    

class Unidade_Organizacional(models.Model):
    nome = models.CharField(max_length=200)
    abreviacao = models.CharField(max_length=200, blank=True)

class Sala(models.Model):
    identificador = models.CharField(max_length=200)

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    nascimento = models.DateTimeField('data de nascimento')
    foto = models.CharField(max_length=200, blank=True)

class Cargo(models.Model):
    nome = models.CharField(max_length=200)

