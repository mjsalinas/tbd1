from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
import pyodbc
import mysql.connector


class Persona(object):
    def __init__(self, nombre, apellido, telefono, correo, ciudad):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.ciudad = ciudad


def cargar_tablas(request, conn, num):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_NAME <> 'sysdiagrams'")
    local_tablas = []
    for row in cursor:
        local_tablas.append(f'{row}')
    
    for x in range(num):
        local_tablas[x] = local_tablas[x].split(",")
        local_tablas[x] = local_tablas[x][0]
        local_tablas[x] = local_tablas[x].split("(")
        local_tablas[x] = local_tablas[x][1]
        local_tablas[x] = local_tablas[x].split("'")
        local_tablas[x] = local_tablas[x][1]
    return local_tablas


def cargar_tipos_dato(request):
    conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                          "Server=localhost\SQLEXPRESS;"
                          "Database=TryingDBS;"
                          "Trusted_Connection=yes;"
                          )
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sys.types")
    tipos_dato = []
    for row in cursor:
        tipos_dato.append(f'{row}')

    conn.close()

    for x in range(len(tipos_dato)):
        tipos_dato[x] = tipos_dato[x].split("(")
        tipos_dato[x] = tipos_dato[x][1]
        tipos_dato[x] = tipos_dato[x].split("'")
        tipos_dato[x] = tipos_dato[x][1]

    return tipos_dato
def select_mysql():
    db = mysql.connector.connect(host="localhost",
                                port="3308",
                                user="root",
                                passwd="",
                                database="tryingdbs"
                                )  # name of the data base

    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()

    # Use all the SQL you like
    cur.execute("""CREATE TABLE Clientes(
    idCliente int NOT NULL PRIMARY KEY,
    nombre varchar(30) NOT NULL)"""
)
    for x in cur:
        print(x)
    # print all the first cell of all the rows
    db.close()

def cargar_num_tablas(request):
    conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                          "Server=localhost\SQLEXPRESS;"
                          "Database=TryingDBS;"
                          "Trusted_Connection=yes;"
                          )
    cursor = conn.cursor()
    cursor.execute(
        "SELECT COUNT(*) from Information_Schema.Tables where TABLE_TYPE = 'BASE TABLE' AND TABLE_NAME <> 'sysdiagrams'")
    for row in cursor:
        num_tablas = f'{row}'
    num_tablas = num_tablas.split(",")
    num_tablas = num_tablas[0].split("(")
    num_tablas = int(num_tablas[1])
    tc = cargar_tablas(request, conn, num_tablas)
    tdd = cargar_tipos_dato(request)
    pks = cargar_llaves_por_tabla(request)
    conn.close()
    return render(request, "homepage.html", dict(tablas=tc, tipos_dato=tdd, llaves_tabla=pks))


def cargar_info(request):
    return(cargar_num_tablas(request))


def cargar_llaves_por_tabla(request):
    resultado_consulta=[]
    conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                          "Server=localhost\SQLEXPRESS;"
                          "Database=TryingDBS;"
                          "Trusted_Connection=yes;"
                          )
    cursor = conn.cursor()
    cursor.execute("""SELECT KU.TABLE_NAME, KU.COLUMN_NAME, KU.CONSTRAINT_NAME
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS AS TC
INNER JOIN
    INFORMATION_SCHEMA.KEY_COLUMN_USAGE AS KU
          ON TC.CONSTRAINT_TYPE = 'PRIMARY KEY' AND
             TC.CONSTRAINT_NAME = KU.CONSTRAINT_NAME AND
			 TC.TABLE_NAME <> 'sysdiagrams'
ORDER BY KU.TABLE_NAME""")
    for row in cursor:
        resultado_consulta.append(f'{row}')
    
    num = len(resultado_consulta)
    for x in range(num):
        resultado_consulta[x] = resultado_consulta[x].split('(')
        resultado_consulta[x] = resultado_consulta[x][1]
        resultado_consulta[x] = resultado_consulta[x].split(')')
        resultado_consulta[x] = resultado_consulta[x][0]
        resultado_consulta[x] = resultado_consulta[x].replace("'", '')
        resultado_consulta[x] = resultado_consulta[x].split(',')
    conn.close()
    llaves_primarias_por_tabla = formato_llave_primaria(resultado_consulta, num)
    return llaves_primarias_por_tabla

def formato_llave_primaria(resultado_consulta, num):
    llaves_primarias = []
    for x in range(num):
        llaves_primarias.append({f'{resultado_consulta[x][0]}' : resultado_consulta[x][1] + " - " + resultado_consulta[x][2]})
    return llaves_primarias

# select_mysql()