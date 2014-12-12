# -*- coding: utf-8 -*-
from django.db import models
from django.core import serializers


# Create your models here.

class Funcao(models.Model):
    nome = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome

class Cargo(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Unidade_Organizacional(models.Model):
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=200, blank=True)
    parent = models.ForeignKey('self', null=True, related_name='children')
    telefone = models.CharField(max_length=30)
    ramal = models.CharField(max_length=5)
    localidade = models.CharField(max_length=300)

    def __str__(self):
        if self.sigla is None:
            return self.nome
        return self.sigla

    def get_parent(self):
        return self.parent

    def get_sons(self):
        return Unidade_Organizacional.objects.filter(parent=self)

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


class Lotacao(models.Model):
    comentarios = models.CharField(blank=True, max_length=500)
    funcao = models.ForeignKey(Funcao)
    uorg = models.ForeignKey(Unidade_Organizacional)
    
    def __str__(self):
        return self.nome

    def get_lotacoes_uorg(self, unidade):
        return Lotacao.objects.filter(uorg=unidade)

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    nascimento = models.DateTimeField('data de nascimento')
    foto = models.CharField(max_length=200, blank=True)
    lotacao_atual = models.ForeignKey(Lotacao)
    cargo = models.ForeignKey(Cargo)
    historico = models.ManyToManyField(Lotacao, related_name='lotacoes_anteriores', blank=True)

    def __str__(self):
        return self.nome



