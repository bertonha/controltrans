# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _


class Endereco(models.Model):
    rua = models.CharField(max_length=128)
    numero = models.PositiveIntegerField(_(u'Número'))
    bairro = models.CharField(max_length=128)
    cidade = models.CharField(max_length=64)
    estado = models.CharField(max_length=2)
    cep = models.CharField(_('CEP'), max_length=9)

    class Meta:
        abstract = True


class Transportadora(Endereco):
    cnpj = models.CharField(max_length=14)
    ie = models.CharField(max_length=14)
    razao_social = models.CharField(max_length=256)
    logo = models.ImageField(upload_to='transportadora')
    telefone = models.CharField(max_length=11)
    email = models.EmailField(unique=True)

    def __unicode__(self):
        return self.razao_social


class Caminhao(models.Model):
    TRUCK_TYPE = (
        (1, 'Truck'),
        (2, '3/4'),
        (3, 'Carreta'),
    )

    TRUCK_MARCA = (
        ('MB', 'Mercedes-Benz'),
        ('VV', 'Volvo'),
        ('VW', 'Volkswagem'),
        ('SC', 'SCANIA'),
    )

    placa = models.CharField(max_length=7)
    modelo = models.CharField(max_length=2, choices=TRUCK_MARCA)
    cidade = models.CharField(max_length=64)
    estado = models.CharField(max_length=2)
    tipo = models.CharField(max_length=2, choices=TRUCK_TYPE)
    capacidade = models.PositiveIntegerField()

    def __unicode__(self):
        return self.placa


class Fornecedor(Endereco):
    cnpj = models.CharField(_('CNPJ'), max_length=14)
    ie = models.CharField(_('IE'), max_length=14)
    razao_social = models.CharField(_(u'Razão Social'), max_length=256)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(unique=True)

    def __unicode__(self):
        return self.razao_social


class Cliente(Endereco):
    cnpj = models.CharField(max_length=14)
    ie = models.CharField(max_length=14)
    razao_social = models.CharField(max_length=256)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(unique=True)


class Nota(models.Model):
    transportadora = models.ForeignKey(Transportadora)
    fornecedor = models.ForeignKey(Fornecedor)
    cliente = models.ForeignKey(Cliente)
    caminha = models.ForeignKey(Caminhao)
    #seguro
    #itens
    natureza_mercadoria = models.CharField(max_length=16, default='Etanol')
    dt_emissao = models.DateTimeField()
