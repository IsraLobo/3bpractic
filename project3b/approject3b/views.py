from django.contrib.auth.models import User
from django.shortcuts import render
from .QueriesBD import QueriesBD


def loginPrin(request):
    try:
        return render(request, 'loginPrin.html', {'alert':None})
    except Exception as e:
        return render(request, 'loginPrin.html', {'alert':'[ERROR]: ' + str(e)})


def logout(request):
    try:
        del request.session['user']
    except:
        pass
    return render(request, 'loginPrin.html', {'alert':'[Aviso]: Session cerrada'})


def registro(request):
    try:
        return render(request, 'registro.html', {'alert':None})
    except Exception as e:
        return render(request, 'loginPrin.html', {'alert':'[ERROR]: ' + str(e)})


def registroSave(request):
    try:
        my_dic = {}
        my_dic = request.POST

        create_user = QueriesBD()
        create_user_st = create_user.createUser(my_dic)

        if create_user_st != True:
            return render(request, 'registro.html', {'alert':'[Aviso]: Este Usuario ya esta registrado, favor de verificar la informacion'})

        return render(request, 'loginPrin.html', {'alert':'[Aviso]: El Usuario se guardo de forma correcta'})
    except Exception as e:
        return render(request, 'loginPrin.html', {'alert':'[ERROR]: ' + str(e)})


def home(request):
    try:
        print(request.POST['csrfmiddlewaretoken'])
        print(request.POST)
        usuario = ''
        try:
            username = request.POST['username'].lower()
            password = request.POST['password'].lower()
            User.objects.get(username=username, password=password)
            usuario = username
        except:
            return render(request, 'loginPrin.html', {'alert':'[ERROR]: Este Usuario No esta registrado'})

        return render(request, 'home.html', {'alert':None, 'usuario':usuario})
    except Exception as e:
        return render(request, 'loginPrin.html', {'alert':'[ERROR]: ' + str(e)})


def products(request, usuario, action):
    try:
        aviso = ''
        if action == 1:
            return render(request, 'saveProduct.html', {'alert':None, 'usuario':usuario})
        elif action == 2:
            my_dict = request.POST
            saveP = QueriesBD()
            aviso = saveP.productSave(my_dict, usuario)
            return render(request, 'home.html', {'alert':aviso, 'usuario':usuario})
    except Exception as e:
        return render(request, 'loginPrin.html', {'alert':'[ERROR]: ' + str(e)})


def inventories(request, usuario, action):
    try:
        aviso = ''
        if action == 1:
            return render(request, 'inventories.html', {'alert':None, 'usuario':usuario})
        elif action == 2:
            stocks_bd = QueriesBD()
            my_dict = request.POST
            aviso = stocks_bd.updateinventories(my_dict)
            return render(request, 'home.html', {'alert':aviso, 'usuario':usuario})
    except Exception as e:
        return render(request, 'home.html', {'alert':'[ERROR]: ' + str(e)})


def orders(request, usuario, action):
    try:
        aviso = ''
        if action == 1:
            return render(request, 'orders.html', {'alert':None, 'usuario':usuario})
        elif action == 2:
            orders_db = QueriesBD()
            my_dict = request.POST
            aviso = orders_db.updateOrders(my_dict, usuario)
            return render(request, 'home.html', {'alert':aviso, 'usuario':usuario})
    except Exception as e:
        return render(request, 'home.html', {'alert':'[ERROR]: ' + str(e)})


def history(request, usuario):
    try:
        histori = QueriesBD()
        aviso = ''
        all_history = histori.inventories()
        if len(all_history) == 0:
            aviso = 'No existe informacion.'
        else:
            aviso = None
        return render(request, 'home.html', {'alert':aviso, 'usuario':usuario, 'history':all_history})
    except Exception as e:
        return render(request, 'home.html', {'alert':'[ERROR]: ' + str(e)})


def historyOrders(request, usuario):
    try:
        histori_order = QueriesBD()
        aviso = ''
        all_orders = histori_order.historyOrders()
        if len(all_orders) == 0:
            aviso = 'No existe informacion.'
        else:
            aviso = None
        return render(request, 'home.html', {'alert':aviso, 'usuario':usuario, 'historyorder':all_orders})
    except Exception as e:
        return render(request, 'home.html', {'alert':'[ERROR]: ' + str(e)})