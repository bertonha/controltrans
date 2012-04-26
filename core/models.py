# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _


#class Endereco(models.Model):
#    rua = ''
#    numero = 0
#   bairro = ''
#    cidade = ''
#    estado = ''
#    cep = ''


class Transportadora(models.Model):
    cnpj = models.CharField(max_length=14)
    ie = models.CharField(max_length=14)
    razao_social = models.CharField(max_length=256)
    slogan = models.ImageField(upload_to='transportadora')
    telefone = models.CharField(max_length=11)
    email = models.EmailField(unique=True)
    #endereco = Endereco()

    def __unicode__(self):
        return self.razao_social


#class Caminha(models.Model):
#    pass


#class Motorista(models.Model):
#    pass


#class Fornecedor(models.Model):
#    pass


#class Cliente(models.Model):
#    pass
