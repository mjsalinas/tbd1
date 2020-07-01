from django.http import HttpResponse
import pyodbc
from ProyectoSqlServer.views.transacts import cargar_info
from ProyectoSqlServer.views.relaciones import crear_relacion_unouno, crear_relacion_muchosmuchos
from django.template import Template, Context, loader
from django.shortcuts import render
import mysql.connector

class Columna(object):
    def __init__(self, nombreTabla, nombreColumna, tipoDato, longitudCampo, isPK, isNullable, isForeign):
        self.nombreTabla = nombreTabla
        self.nombreColumna = nombreColumna
        self.tipoDato = tipoDato
        self.longitudCampo = longitudCampo
        self.isPK = isPK
        self.isNullable = isNullable
        self.isForeign = isForeign


def crear_tablas(request):
    columnas_ordenadas = []
    llaves_primarias = []
    llaves_foraneas = []
    longitud_campo = []
    nombre_tabla = request.POST.get('nombre_tabla')
    nombre_columnas = request.POST.getlist('nombre_columna[]')
    tipo_dato = request.POST.getlist('tipo_dato[]')
    longitud_campo = request.POST.getlist('longitudCampo[]')
    relacion = request.POST.getlist('relacion[]')
    nullable = request.POST.getlist('nullable[]')
    foreign = request.POST.getlist('foreign[]')
    tipo_relacion = request.POST.get('relationType')

    nCols = int(len(nombre_columnas))
    for n in range(nCols):
        columna = Columna(
            nombre_tabla, nombre_columnas[n], tipo_dato[n], longitud_campo[n], relacion[n], nullable[n], foreign[n])
        columnas_ordenadas.append(columna)

    query = f'CREATE TABLE {columnas_ordenadas[0].nombreTabla} ('
    for columna in columnas_ordenadas:

        if columna.isNullable == "true":
            query += f'\n{columna.nombreColumna} {columna.tipoDato} ({columna.longitudCampo}),'
        if columna.isNullable == "false":
            if columna.tipoDato == "char" or columna.tipoDato == "varchar":
                query += f'\n{columna.nombreColumna} {columna.tipoDato}({columna.longitudCampo}) NOT NULL,'
            else:
                query += f'\n{columna.nombreColumna} {columna.tipoDato} NOT NULL,'
        if columna.isPK == "true":
            llaves_primarias.append(columna)
        if columna.isForeign == "true":
            llaves_foraneas.append(columna)

    if len(llaves_primarias) > 0:
        query = crear_llave_primaria(
            query, llaves_primarias, len(llaves_foraneas))
    print(tipo_relacion)
    if len(llaves_foraneas) > 0:
        if tipo_relacion == "oneOnOne":
            query = crear_relacion_unouno(request, query, llaves_foraneas)
        if tipo_relacion == "oneOnMany":
            query = crear_relacion_unouno(request, query, llaves_foraneas)
        if tipo_relacion == "manyOnMany":
            query = crear_relacion_muchosmuchos(
                request, query, llaves_foraneas)
    query += ');'
    print(query)
    mysqlConn = mysql.connector.connect(host="localhost",
                                port="3308",
                                user="root",
                                passwd="",
                                database="tryingdbs"
                                )

    conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                        "Server=localhost\SQLEXPRESS;"
                        "Database=TryingDBS;"
                        "Trusted_Connection=yes;"
                        )
    mysqlCursor = mysqlConn.cursor()
    cursor = conn.cursor()
    mysqlCursor.execute(query)
    cursor.execute(query)
    cursor.execute('commit')
    conn.close()
    mysqlConn.close()
    return cargar_info(request)


def crear_llave_primaria(query, llaves, numFK):

    for columna in llaves:
        if (numFK) > 0:
            query += '\nPRIMARY KEY(' + columna.nombreColumna + '),'
        if (numFK) == 0:
            query += '\nPRIMARY KEY('+ columna.nombreColumna +')'
    return(query)
