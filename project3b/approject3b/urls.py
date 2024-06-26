from django.urls import path
from .views import products, inventories, orders, loginPrin, logout, home, registro, registroSave, history, historyOrders


urlpatterns = [
    path('', loginPrin, name='loginPrin'),
    path('logout/', logout, name='logout'),
    path('registro/', registro, name='registro'),
    path('registroS/', registroSave, name='registroSave'),
    path('home/', home, name='home'),
    path('products/<str:usuario>/<int:action>/', products, name='products'),
    path('inventories/<str:usuario>/<int:action>/', inventories, name='inventories'),
    path('orders/<str:usuario>/<int:action>/', orders, name='orders'),
    path('history/<str:usuario>/', history, name='history'),
    path('historyOrders/<str:usuario>/', historyOrders, name='historyOrders'),
]