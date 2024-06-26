from django.contrib.auth.models import User
from .models import products, historyOrder


class QueriesBD():

    def createUser(self, my_dic):
        try:
            if not User.objects.filter(username=my_dic['username'].lower(), password=my_dic['password'].lower(), first_name=my_dic['first_name'].lower(), last_name=my_dic['last_name'].lower()).exists():
                user_create = User.objects.create(username=my_dic['username'].lower(), password=my_dic['password'].lower(), first_name=my_dic['first_name'].lower(), last_name=my_dic['last_name'].lower())
                return True
            else:
                return False
        except Exception as e:
            return False


    def productSave(self, my_dic, usuario):
        try:
            if not products.objects.filter(sku_product=my_dic['codigo']).exists():
                pd_user = User.objects.get(username=usuario)
                product, status = products.objects.update_or_create(sku_product=my_dic['codigo'],
                                                                    name_product=my_dic['producto'],
                                                                    user_save=pd_user.username.capitalize(),
                                                                    id_user=pd_user.id)

                return 'El Producto se guardo con exito'
            else:
                return 'El Producto con el Codigo ya existe, Favor de revisar los Valores'
        except Exception as e:
            return str(e)



    def inventories(self):
        try:
            get_products = products.objects.all().order_by('sku_product')
            return get_products
        except Exception as e:
            return []


    def updateinventories(self, my_dic):
        try:
            if products.objects.filter(sku_product=my_dic['codigo']).exists():
                upd_stock = products.objects.get(sku_product=my_dic['codigo'])
                upd_stock.stock_product = upd_stock.stock_product + int(my_dic['stock'])
                upd_stock.save()
                return 'Se modifico correctamente el Producto: ' + upd_stock.name_product
            else:
                return 'No existe el Producto a modificar.'
        except Exception as e:
            return '[ERROR: ]' + str(e)


    def updateOrders(self, my_dict, usuario):
        try:
            alerta = ''
            if products.objects.filter(sku_product=my_dict['codigo']).exists():
                upd_order = products.objects.get(sku_product=my_dict['codigo'])

                if int(my_dict['stock']) > upd_order.stock_product:
                    return 'No se puede realizar la compra, la cantidad solicitada es mayor a lo que existe actualmente en el Almacen. [ALMACEN]: ' + str(upd_order.stock_product)

                upd_order.stock_product = upd_order.stock_product - int(my_dict['stock'])
                
                insert_order = QueriesBD.insertOrder(self, upd_order.sku_product, upd_order.name_product, my_dict['stock'], usuario)

                if insert_order == True:
                    upd_order.save()
                else:
                    return 'No se pudo guardar la compra existen Errores.'

                if upd_order.stock_product < 10:
                    alerta = '[AVISO]: La cantidad de producto en el almacen es menor a 10 pz.'

                return 'Se realizo la compra con exito. ' + alerta
            else:
                return 'No existe el Producto que desea comprar.'
        except Exception as e:
            print(str(e))
            return '[ERROR: ]' + str(e)


    def insertOrder(self, id_product, name_product, cantidad, usuario):
        try:
            my_user = User.objects.get(username=usuario)
            historyOrder.objects.create(idproduct=id_product,
                                        productname=name_product,
                                        userproduct=my_user.username.capitalize(),
                                        userid=my_user.id,
                                        cant_order=cantidad)
            return True
        except:
            return False


    def historyOrders(self):
        try:
            get_orders = historyOrder.objects.all().order_by('idproduct')
            return get_orders
        except:
            return []