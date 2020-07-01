from django.urls import path
from ProyectoSqlServer.views.transacts import  cargar_info
from ProyectoSqlServer.views.tablas import crear_tablas

urlpatterns = [
    path('', cargar_info),
    path('crearTabla/', crear_tablas),

    ]
