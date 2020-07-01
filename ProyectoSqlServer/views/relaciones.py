from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
from ProyectoSqlServer.views.transacts import cargar_info


def crear_relacion_unouno(request, query, llaves_foraneas):
    tabla1 = request.POST.getlist('tabla1[]')
    print(tabla1)
    # del tabla1[0]
    llave1 = request.POST.getlist('llave1[]')
    print(llave1)
    
    for n in range(int(len(tabla1))):
        for campo in llaves_foraneas:
            if (n+1) == int(len(tabla1)):
                query += '\nFOREIGN KEY (' + campo.nombreColumna + ')' + ' REFERENCES ' + tabla1[n] + '('+llave1[n]+')'
            if (n+1) < int(len(tabla1)):
                query += '\nFOREIGN KEY (' + campo.nombreColumna + ')' + ' REFERENCES ' + tabla1[n] + '('+llave1[n]+'),'
            llaves_foraneas.remove(campo)
            break
    
    return query

def crear_relacion_muchosmuchos(request, query, llaves_foraneas):
    junctionTableName = llaves_foraneas[0].nombreTabla
    tabla1 = request.POST.getlist('tabla1[]')
    llave1 = request.POST.getlist('llave1[]')
    # tabla1.remove('--tabla--')
    print(junctionTableName)
    print(tabla1)
    print(llave1)
    
    
    
    query = "CREATE TABLE "+ junctionTableName +" ("
    
    for n in range(int(len(tabla1))):
        query += llave1[n] + llaves_foraneas[n].tipoDato + "NOT NULL, \n"
        
    for n in range(int(len(tabla1))):
        for campo in llaves_foraneas:
            if (n+1) == int(len(tabla1)):
                query += '\nFOREIGN KEY (' + campo.nombreColumna + ')' + ' REFERENCES ' + tabla1[n] + '('+llave1[n]+')'
            if (n+1) < int(len(tabla1)):
                query += '\nFOREIGN KEY (' + campo.nombreColumna + ')' + ' REFERENCES ' + tabla1[n] + '('+llave1[n]+'),'
            llaves_foraneas.remove(campo)
            break
    print(query) 
    return query
