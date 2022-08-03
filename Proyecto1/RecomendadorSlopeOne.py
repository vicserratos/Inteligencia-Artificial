#!/usr/bin/env python
# coding: utf-8

import csv
import pandas
from array import *
import random

# Genera la matriz de los datos a analizar        

# Matriz de los usuarios y sus ratings
datos = {}

# Regresa el id del producto
def getIdCompra(compraString):
    switcher = {
        "Beso" : 0,
        "Bolillo" : 1,
        "Cocol" : 2,
        "Concha" : 3,
        "Cuernito" : 4,
        "Dona" : 5,
        "Mantecada" : 6,
        "Oreja" : 7,
        "Polvoron" : 8        
    }
    return switcher.get(compraString, "¡¡¡No existe ese pan!!!")

# Regresa una tupla de diccionario con key:value, 
# key = nombre del usuario y value = Array con sus clasificaciones
def asignaValor(nombre, compra, calif, datos):
    if(nombre in datos.keys()):
        datos[nombre][getIdCompra(compra)] = int(calif)
        #print(nombre, datos[nombre], sep=" : ")
    else:
        arrayCompras = [0] * 9
        arrayCompras[getIdCompra(compra)] = int(calif)
        datos[nombre] = arrayCompras
        #print(nombre, datos[nombre], sep=" : ")

# Lee csv 
with open('./data/BasePan.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 1
    for row in csv_reader:
        asignaValor(row['Nombre'], row['Compra'], row['Calificacion'], datos)

productos = ["Beso", "Bolillo", "Cocol", "Concha", "Cuernito", "Dona", "Mantecada", "Oreja", "Polvoron"]
print(pandas.DataFrame( data=datos.values(), index = datos.keys(), columns=productos))


# Imprime Menú

# Despliega Menu 1
def opcion1():
    print("1) ¿Que deseas hacer?")
    print("\ta. Crear usuario y generar ratings manuales. Obtendras las ~3 mejores recomendaciones\n")
    print("\tb. Obtener un usuario al azar y obtener las ~3 mejores recomendaciones")
    
    op = input("Ingresa a o b:  ")
    if(op != "a"):
        if(op != "b"):
            return 0
    else:
        return op
    
# Crea Usuario manual
def creaUsuario():
    productos = ["Beso", "Bolillo", "Cocol", "Concha", "Cuernito", "Dona", "Mantecada", "Oreja", "Polvoron"]
    arrayRatings = [0] * 9
    nombre = input("\nIntroduce tu nombre:  ")
    print("\nIntroduce los ratings de los productos que compraste de 0 a 5\n")
    print("1 No me gusta -- 5 Delicioso -- 0 = no lo calificas")
    print("Lo mejor serán entre 3 y 5 calificaciones. Tienes que introducir al menos uno y a lo mas 8 calificaciones")
    
    i = 0
    j = 0
    for producto in productos:
        while True:            
            rating = input("Rating de " + producto + ": ")
            if int(rating) in (range(6)): 
                arrayRatings[j] = int(rating)
                if(i == 7):
                    break
                if(int(rating) != 0):
                    i += 1
                j += 1
                break
            else:
                print("\nIntroduce del 0 a 5")
    return (nombre, arrayRatings)

# Despliega Menu
print("Panaderia \"Los Biscochos\"\n\n")
opcion = opcion1()
while True:
    if(opcion == 0):
        print("\n¡Opcion incorrecta! De nuevo\n")
        opcion = opcion1()
    else:
        break
        
if(opcion == "a"):
    datosUsuario = creaUsuario()    
    print(datosUsuario)
else:
    # Selecciona aleatoriamente datos de  algún usuario en la base
    datosUsuario = key, val = random.choice(list(datos.items())) 
    # Eliminala tupla del diccionario en concreto para no afectar el resultado
    del datos[datosUsuario[0]]


# Obtiene la suma de todas las desviaciones
def getDesviacion(idProducto, datos):
    
    # Primer arreglo son el acumulado de las desviaciones, 
    # segundo son el conteo de desviaciones
    arrayDesviaciones = [[0] * 9, [0] * 9]
    
    # Se recorren lo arreglos y se descarta el arreglo 
    # donde el idProducto no tiene calificación ( =0) 
    # ya que así no hay forma de hacer match entre usuarios
    for array in datos.values():
        if(array[idProducto] != 0):           
            #print("----------")
            #print(array)
        
            # Se recorren los valores del arreglo y se descartan los ids similares
            # ya que no se hace una comparación entre si mismo y cuando son ceros
            # ya que eso quiere decir que no ha sido calificado, aún.
            for i in range( len(array) ):
                if(i == idProducto or array[i] == 0):
                    continue
                
                # Entonces se suman las desviaciones y se asigna la cardinalidad
                else:
                    par = array[idProducto] - array[i]
                    #print(array[idProducto], array[i])
                    arrayDesviaciones[0][i] += par
                    arrayDesviaciones[1][i] += 1
                    #print(arrayDesviaciones[0], arrayDesviaciones[1], sep = " . ")
    return arrayDesviaciones

# Ya que se tienen las desviaciones, hay que obtener el promedio de todas
# las sumas de las desviaciones y sumarle el rating que ya dio el usuario
# ¡Se deben descartar donde el usuario no tiene un rating!
def resuelveSlopeOne(idProducto, mDesviaciones, ratingsUsuario): 
    rating = 0
    cardinalidad = 0
    # Se descartan los ratings en 0
    for i in range( len(mDesviaciones[0]) ):
        if(ratingsUsuario[i] == 0):
            continue
        else:
            # la suma de la desviaciones entre el total de estas
            promedio = mDesviaciones[0][i] / mDesviaciones[1][i]
            # Al promedio se le suma el rating del usuario
            suma = promedio + ratingsUsuario[i]
            # Esto equivale a la suma de todas las desviaciones
            rating += suma
            cardinalidad += 1
            #print(suma)
    
    return (1/cardinalidad)*(rating)


print("Ratings de : " + datosUsuario[0])
print("\t" + str(datosUsuario[1]) )
print("Los que tienen \"0\" son los que vamos a evaluar")

print("\nCalculo de Ratings a predecir\n")

resultados = {}

for idProducto in range(len(datosUsuario[1])) :
    if(datosUsuario[1][idProducto] == 0):
        mDesviaciones = getDesviacion(idProducto, datos)
        print("Desviaciones del pan: " + productos[idProducto]+"\n")
        print(pandas.DataFrame( data=mDesviaciones, index = ["Ratings", "Cardinalidades"], columns=productos))
        print("\n")
        ratingCalculado = resuelveSlopeOne(idProducto, mDesviaciones, datosUsuario[1])     
        print("*Rating del pan: " + str(ratingCalculado) +"\n")
        
        resultados[productos[idProducto]] = ratingCalculado
        
ordenados = sorted(resultados.items(), key=lambda x: x[1], reverse=True)
print(ordenados)


print("\nBienvenid@ : " + datosUsuario[0])  

print("\nQue deseas comprar?\n")
#Es para mostrar el ejemplo
print("..........")
print("..........")
print("..........\n")
    
print("\nTe recomendamos los siguientes productos: \n")   
try:
    for x in range(3):
        print("\t" + str(x + 1) + ". ¡¡¡" + str(ordenados[x][0]) + "!!! -> Da Click")
except IndexError as error:
        print()
