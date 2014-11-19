from django.db import models

# Create your models here.

class Funcao(models.Model):
    nome = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome

class Lotacao(models.Model):
    nome = models.CharField(max_length=200)
    funcao = models.ForeignKey(Funcao)

    def __str__(self):
        return self.nome

class Unidade_Organizacional(models.Model):
    nome = models.CharField(max_length=200)
    abreviacao = models.CharField(max_length=200, blank=True)
    parent = models.ForeignKey('self', null=True, related_name='children')

    def __str__(self):
        if self.abreviacao is None:
            return self.nome
        return self.abreviacao

    def get_parent(self):
        return self.parent

    def get_sons(self):
        return Unidade_Organizacional.objects.filter(parent=self)

class Sala(models.Model):
    identificador = models.CharField(max_length=200)
    unidade = models.ForeignKey(Unidade_Organizacional)

    def __str__(self):
        return self.identificador

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    nascimento = models.DateTimeField('data de nascimento')
    foto = models.CharField(max_length=200, blank=True)
    lotacao_atual = models.ForeignKey(Lotacao)
    historico = models.ManyToManyField(Lotacao, related_name='lotacoes_anteriores')

    def __str__(self):
        return self.nome

class Cargo(models.Model):
    nome = models.CharField(max_length=200)
    oucupante = models.ForeignKey(Pessoa)

    def __str__(self):
        return self.nome


