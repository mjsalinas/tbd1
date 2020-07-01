from django.http import HttpResponse
import datetime
import pyodbc
from django.template import Template, Context, loader
from django.shortcuts import render
class Persona(object):
    def __init__(self, nombre, apellido, telefono, correo, ciudad):
        self.nombre=nombre
        self.apellido=apellido
        self.telefono=telefono
        self.correo=correo
        self.ciudad=ciudad

tablas=[]
def leer_bd(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("select * from t_Cliente")
    for row in cursor:
        print(f'row= {row}')
    print()

def crear_bd(conn, p1):
    print("Create")
    
    cursor = conn.cursor()
    cursor.execute(
        'insert into t_Cliente(nombre,apellido,telefono,correo,ciudad) values (?,?,?,?,?);',
        (p1.nombre , p1.apellido , p1.telefono , p1.correo , "SPS")
    )
    conn.commit()
    leer_bd(conn)

def actualizar_bd(conn):
    print("Update")
    cursor = conn.cursor()
    cursor.execute(
        'update t_Cliente set apellido = ? where nombre = ?;',
        ('Quiroz', 'Maria')
    )
    conn.commit()
    leer_bd(conn)

def eliminar_bd(conn):
    print("Delete")
    cursor = conn.cursor()
    cursor.execute(
        "DELETE from t_Cliente WHERE t_Cliente.nombre = 'Juan';"
    )
    conn.commit()
    leer_bd(conn)
    

    
def cargar_tablas(request, conn, num):
    print("Obteniendo tablas")
    cursor = conn.cursor()
    # cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_NAME <> 'sysdiagrams'")
    cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES")
    local_tablas=[]
    for row in cursor:
        local_tablas.append(f'{row}')
    
    for x in range(num):
        local_tablas[x] = local_tablas[x].split(",")
        local_tablas[x] = local_tablas[x][2]
     
    tablas = local_tablas
    contexto = {"tablas": tablas}
    return contexto

def cargar_num_tablas(request):
    conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=localhost\SQLEXPRESS;"
                      "Database=POS;"
                      "Trusted_Connection=yes;"
                      )
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) from Information_Schema.Tables where TABLE_TYPE = 'BASE TABLE'")
    for row in cursor:
       num_tablas = f'{row}'
    num_tablas = num_tablas.split(",")   
    num_tablas = num_tablas[0].split("(")
    num_tablas = int(num_tablas[1])
    contexto = cargar_tablas(request, conn, num_tablas)       
    conn.close()
    return render(request, "homepage.html", contexto)
    
    
def cargar_info(request):
    return cargar_num_tablas(request)

def recibir(request):
    if request.method=="POST":
        persona_a_ingresar=Persona(request.POST["nombre_persona"],
                                   request.POST["apellido_persona"],
                                   request.POST["telefono_persona"],
                                   request.POST["correo_persona"],
                                   "TGU")
        conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                        "Server=localhost\SQLEXPRESS;"
                        "Database=POS;"
                        "Trusted_Connection=yes;"
                        )
        crear_bd(conn, persona_a_ingresar)
        conn.close()
        
    return (cargar_info(request))    

# leer_bd(conn)
# crear_bd(conn)
# actualizar_bd(conn)
# eliminar_bd(conn)