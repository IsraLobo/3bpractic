from django.db import models
from datetime import datetime


class products(models.Model):
    sku_product = models.IntegerField('Id Producto', blank= True, null= True)
    name_product = models.CharField('Nompre del Producto', max_length=200, blank= True, null= True)
    stock_product = models.IntegerField('Stock del Producto',default=100, blank= True, null= True)
    user_save = models.CharField('Usuario que Guardo', max_length=200, blank= True, null= True)
    id_user = models.IntegerField('Id Usuario', blank= True, null= True)

    def __str__(self):
        return self.name_product


class historyOrder(models.Model):
    idproduct = models.IntegerField('Id Producto', blank= True, null= True)
    productname = models.CharField('Nompre del Producto', max_length=200, blank= True, null= True)
    userproduct = models.CharField('Usuario que Compro', max_length=200, blank= True, null= True)
    userid = models.IntegerField('Id Usuario', blank= True, null= True)
    fecha_order = models.DateTimeField('Fecha de compra', default=datetime.now(), blank= True, null= True)
    cant_order = models.IntegerField('Cantidad de Compra', blank= True, null= True)

    def __str__(self):
        return self.name_product
