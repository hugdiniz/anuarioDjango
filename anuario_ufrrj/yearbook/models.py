# -*- coding: utf-8 -*-
from django.db import models
from django.core import serializers


# Create your models here.
class Cargo(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Funcao(models.Model):
    nome = models.CharField(max_length=200)
    data_inicio = models.DateField('data_inicio')
    data_saida = models.DateField('data_saida')

    
    def __str__(self):
        return self.nome

class Unidade_Organizacional(models.Model):
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=200, blank=True)
    parent = models.ForeignKey('self', null=True, related_name='children')
    telefone = models.CharField(max_length=30)
    ramal = models.CharField(max_length=5)
    localidade = models.CharField(max_length=300, blank=True)
    localidade_sala = models.ForeignKey('Sala', null=True, blank=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        if self.sigla is None:
            return self.nome
        return self.sigla

    def get_parent(self):
        return self.parent

    def get_sons(self):
        return Unidade_Organizacional.objects.filter(parent=self)

    def get_salas(self):
        return Sala.objects.filter(uorg=self)

    def recuperar_unidades_raiz(self):
        return Unidade_Organizacional.objects.filter(parent=None)



class Sala(models.Model):
    identificador = models.CharField(max_length=200)
    predio = models.CharField(max_length=200)
    andar = models.IntegerField()
    uorg = models.ForeignKey(Unidade_Organizacional)

    def __str__(self):
        return self.identificador

    def get_uorg(self):
        return self.uorg


class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=30)
    ramal = models.CharField(max_length=5)
    nascimento = models.DateTimeField('data de nascimento')
    foto = models.CharField(max_length=200, blank=True)
    cargo = models.ForeignKey(Cargo)
    email = models.CharField(max_length=100, null=True, blank=True)
    
    ferias_inicio = models.DateField('inicio das ferias', blank=True, null=True)
    ferias_fim = models.DateField('fim das ferias', blank=True, null=True)

    licenca_inicio = models.DateField('inicio licenca', null=True, blank=True)
    licenca_fim = models.DateField('fim licenca', null=True, blank=True)

    historico = models.ManyToManyField('Lotacao', related_name='lotacoes_anteriores', blank=True)

    def __str__(self):
        return self.nome


class Lotacao(models.Model):

    nome = models.CharField(max_length=200)
    pessoa = models.ForeignKey(Pessoa)
    uorg = models.ForeignKey(Unidade_Organizacional)
    sala = models.ForeignKey(Sala, blank=True, null=True)
    funcao = models.ForeignKey(Funcao, blank=True, null=True)

    entrada = models.DateField('data de entrada', null=True, blank=True, auto_now_add=True)
    afastamento = models.DateField('data de afastamento', null=True, blank=True)

    
    def __str__(self):
        return self.nome

    def get_lotacoes_uorg(self, unidade):
        return Lotacao.objects.filter(uorg=unidade)


class User(models.Model):
    nome = models.CharField(max_length=200)
    password = models.CharField(max_length=16)
    uorg = models.ForeignKey(Unidade_Organizacional)