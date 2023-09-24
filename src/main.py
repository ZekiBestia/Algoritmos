#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 15:33:19 2023

@author: zekibestia
"""

from Methods import MathSolver
from MethodsIn import UserInterface
calcular= MathSolver()
user=UserInterface()
contador=0

# Crea un diccionario que mapea las opciones a las descripciones
opciones = {
    '1': "Raiz Cuadrada",
    '2': "Ecuacion 2do Grado",
    '3': "Pi",
    '4': "Factorial",
    '5': "Contador de Veces",
    '6': "Dos Números Grandes Consecutivos",
    '7': "Índice del Predecesor Menor",
    '8': "Suma de Serie",
    '9': "Permutaciones",
    '10': "Combinaciones",
    '11': "Salir"
}

while True:
    user.limpiar_pantalla()
    user.portada()
    print("----------MENU------------")
    for opcion, descripcion in opciones.items():
        print(f"------{opcion}. {descripcion}")

    opcion = input("Elige una opción (1-11): ")
    descripcion = opciones.get(opcion, "Opción no válida")
    
    if opcion == '1':
        print("Calcular Raiz Cuadrada")
        n=user.pedir_numero()
        raizM=calcular.raizMath(n)
        raizNewtonRapson=calcular.raizNewton_Rapson(n)
        print(f"La raiz con Math es: {raizM}")
        print(f"La raiz con el metodo Newton-Rapson es: {raizNewtonRapson}")
    elif opcion == '2':
        # Agrega aquí tu código para resolver la ecuación de segundo grado
        print("Función para resolver ecuación de segundo grado.")
        print("ax^2 + bx + c = 0.")
        a,b,c=user.pedirABC()
        ecu = calcular.calcular_raices(a, b, c)  # Método sin math
        ecuNumpy=calcular.ecuNumpy(a, b, c)
        print(f"La solución de la ecuación sin math es: {ecu}")
        print(f"La solución de la ecuación con numpy es: {ecuNumpy}")
        
    elif opcion == '3':
        
        pimath=calcular.calcular_pi_Math()
        leibniz=calcular.calcular_pi_leibniz(100000)
        print(f"El valor de PI por leibniz{leibniz}")
        
    elif opcion == '4':
        n =user.pedir_numero()
        facMath=calcular.calcularFactorialMath(n)
        fac=calcular.calcularFactorial(n)
        print(f"Factorial por Math {facMath}")
        print(f"Factorial {fac}")    

    elif opcion == '5':
        # Agrega aquí tu código para contar las veces que ocurre un elemento en una lista
        print("Función para contar las veces que ocurre un elemento en una lista.")
        n,r,c=user.pedirListRangeNum()
        lista=calcular.listaAleatorios(n,r)
        conta=calcular.contar_apariciones(lista, c)
        print(f"La lista es la siguente : {lista}")
        print(f"El numero de apariciones de {c} es : {conta}")

    elif opcion == '6':
        # Agrega aquí tu código para encontrar dos números grandes consecutivos en una lista
        print("Función para encontrar dos números grandes consecutivos en una lista.") 
        print("Agrega la lista:")
        num=user.pedirListaN()
        print(num)
        conse=calcular.dos_numeros_mas_grandes_consecutivos(num)
        if isinstance(conse, str):
                print(conse)  # Imprime el mensaje error si no hay números consecutivos
        else:
                max1, max2, max_general=conse
                print(f"Los dos números más grandes consecutivos son: {max1} y {max2}")
                print(f"El número más grande dentro de la lista es: {max_general}")

    elif opcion == '7':
        # Agrega aquí tu código para encontrar el índice del predecesor menor en una lista de cadenas
        print("Función para encontrar el índice del predecesor menor en una lista de cadenas.\nEl indice comienza en 0")
        print("Ejemplo:")
        lista=["TOMAS","BRUNO","ELIE","DAN","ZEKE"]
        iPredecesorMenor=calcular.indice_procesador_menor(lista)
        print(f"Lista: {lista}")
        print("El indice del predecesor menor es: " + str(iPredecesorMenor))
        n=user.pedirLista()
        print(n)
        prede=calcular.indice_procesador_menor(n)
        print("El indice del predecesor menor es: "+str(prede))

    elif opcion == '8':
        # Agrega aquí tu código para calcular la suma de una serie
        print("Función para calcular la suma de una serie.")
        s=user.pedirListaN()
        print(f"Lista de numeros: {s}")
        n=len(s)
        v1=calcular.maxSumaV1(s, n)
        v2=calcular.maxSumaV2(s, n)
        v3=calcular.maxSumaV3(s, n)
        print(f"Suma maxima de numeros consecutivos\nVersion1: {v1}\nVersion2: {v2}\nVersion3: {v3}")
        print(v3)
    elif opcion == '9':
        print("Permutaciones")
        n,r=user.pedirNyR()
        perm=calcular.generarPermuta(n, r)
        for i in perm:
         contador+=1
         print(i)
        print(f"Permutaciones metodo propio:  {contador}")
        contador=0
        print("Permutaciones Generadas por Libreria Permutations")
        permLib=calcular.generarPerLibreria(n, r)
        
    elif opcion =='10':
        print("Combinaciones")
        n,r=user.pedirNyR()
        combi=calcular.generarCombina(n,r)
        for i in combi:
         print(i)
         contador+=1
        print(f"Combinaciones Generada metodo propio : {contador}")
        contador=0
        combL=calcular.generarCombLibreria(n, r)
        
    elif opcion == '11':
        print("Saliendo del programa. ¡Hasta luego!")
        break
        
    else:
        print("Opción no válida. Introduce un número del 1 al 11.")

    # Preguntar al usuario si desea volver al menú o salir
    respuesta = input("¿Desea volver al menú (S/N)? ").strip().lower()
    if respuesta != 's':
        print("Saliendo del programa. ¡Hasta luego!")
        break


