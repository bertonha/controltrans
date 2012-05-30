# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _


class Endereco(models.Model):
    rua = models.CharField(max_length=128)
    numero = models.PositiveIntegerField(_(u'Número'))
    bairro = models.CharField(max_length=128)
    cidade = models.CharField(max_length=64)
    uf = models.CharField(max_length=2)
    cep = models.CharField(_('CEP'), max_length=9)

    def __unicode__(self):
        return '{}, {} - {} - {} - {}'.format(self.rua,
                                         self.numero,
                                         self.bairro,
                                         self.cidade,
                                         self.uf)


class CommonFields(models.Model):
    cnpj = models.CharField(_('CNPJ'), max_length=14)
    ie = models.CharField(_('IE'), max_length=14)
    nome = models.CharField(_(u'Razão Social'), max_length=256)
    fantasia = models.CharField(_(u'Nome Fantasia'), max_length=256, blank=True)
    fone = models.CharField(max_length=11, blank=True)
    email = models.EmailField(unique=True, blank=True)
    endereco = models.ForeignKey(Endereco)

    def __unicode__(self):
        return self.nome

    class Meta:
        abstract = True


class Transportadora(CommonFields):
    logo = models.ImageField(upload_to='transportadora', blank=True)


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


class Fornecedor(CommonFields):
    pass


class Cliente(CommonFields):
    pass


class Nota(models.Model):
    transportadora = models.ForeignKey(Transportadora)
    fornecedor = models.ForeignKey(Fornecedor)
    cliente = models.ForeignKey(Cliente)
    caminha = models.ForeignKey(Caminhao)
    #seguro
    #itens
    natureza_mercadoria = models.CharField(max_length=16, default='Etanol')
    dt_emissao = models.DateTimeField(_(u'Data Emissão'), auto_now_add=True)
