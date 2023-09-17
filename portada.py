#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 15:33:19 2023

@author: zekibestia
"""

from Metodos import Metodos
import math
import os
#OBJETO
calcular= Metodos()
calcular2= Metodos()

def limpiar_pantalla():
    sistema = os.name
    if sistema == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux
        os.system('clear')

def pedir_numero():
    while True:
        try:
            numero = int(input("Digite el número: "))
            return numero  # Retorna el número si la entrada es válida
        except ValueError:
            print("Error: Debe ingresar un número válido. Inténtelo de nuevo.")
            
def pedirABC():
    while True:
        try:
            a = int(input("Digite el número para a : "))# Retorna el número si la entrada es válida
            b= int(input("Digite el número para b : "))
            c = int(input("Digite el número para c: "))
            return a,b,c
        except ValueError:
            print("Error: Debe ingresar un número válido. Inténtelo de nuevo.")

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
    '9': "Salir"
}

while True:
    limpiar_pantalla()
    print("-------MENU--------")
    for opcion, descripcion in opciones.items():
        print(f"{opcion}. {descripcion}")

    opcion = input("Elige una opción (1-9): ")

    descripcion = opciones.get(opcion, "Opción no válida")

    if opcion == '1':
        print("Calcular Raiz Cuadrada")
        n=pedir_numero()
        raizM=calcular.raizMath(n)
        raizNewtonRapson=calcular.raizNewton_Rapson(n)
        print(f"La raiz con Math es: {raizM}")
        print(f"La raiz con el metodo Newton-Rapson es: {raizNewtonRapson}")
        

    elif opcion == '2':
        # Agrega aquí tu código para resolver la ecuación de segundo grado
        print("Función para resolver ecuación de segundo grado.")
        print("ax^2 + bx + c = 0.")
        a,b,c=pedirABC()
        ecu = calcular.calcular_raices(a, b, c)  # Método sin math
        ecuNumpy=calcular.ecuNumpy(a, b, c)
        print(f"La solución de la ecuación sin math es: {ecu}")
        print(f"La solución de la ecuación con numpy es: {ecuNumpy}")
        

    elif opcion == '3':
        
        pimath=calcular.calcular_pi_Math()
        leibniz=calcular.calcular_pi_leibniz(100000)
        print(f"El valor de PI por leibniz{leibniz}")
        

    elif opcion == '4':
        n = pedir_numero()
        facMath=calcular.calcularFactorialMath(n)
        fac=calcular.calcularFactorial(n)
        print(f"Factorial por Math {facMath}")
        print(f"Factorial {fac}")
        

    elif opcion == '5':
        # Agrega aquí tu código para contar las veces que ocurre un elemento en una lista
        print("Función para contar las veces que ocurre un elemento en una lista.")

    elif opcion == '6':
        # Agrega aquí tu código para encontrar dos números grandes consecutivos en una lista
        print("Función para encontrar dos números grandes consecutivos en una lista.")

    elif opcion == '7':
        # Agrega aquí tu código para encontrar el índice del predecesor menor en una lista de cadenas
        print("Función para encontrar el índice del predecesor menor en una lista de cadenas.")
        lista=["JuanCARLOS","Pedro","Juan"]
        iPredecesorMenor=calcular.indice_procesador_menor(lista)
        print("El indice del predecesor menor es: " + str(iPredecesorMenor))

    elif opcion == '8':
        # Agrega aquí tu código para calcular la suma de una serie
        print("Función para calcular la suma de una serie.")

    elif opcion == '9':
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Introduce un número del 1 al 9.")

    # Preguntar al usuario si desea volver al menú o salir
    respuesta = input("¿Desea volver al menú (S/N)? ").strip().lower()
    if respuesta != 's':
        print("Saliendo del programa. ¡Hasta luego!")
        break


