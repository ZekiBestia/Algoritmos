#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 11:13:05 2023

@author: zekibestia
"""
# Permutaciones
'''
 PERMUTACIONES
     nPr= n!/(n-r)!
     Organizar elementos en orden
 COMBINACIONES
     Seleccionar objetos de un grupo y el orden no importa
     nCr= nPr/r!
     
'''
from itertools import permutations, combinations
import numpy as np
import math
import random

class MathSolver:
  #  Methods for solving mathematical problems
    
    '''
    1.RaizCuadrada
    '''
    @staticmethod
    def raizMath(numero):
        # Calcular la raíz cuadrada del número proporcionado
        raiz_cuadrada = math.sqrt(numero)
        return raiz_cuadrada
    
    @staticmethod 
    def raizNewton_Rapson(n):
        aproximacion = n / 2
        precision = 0.00001  

        while abs(aproximacion * aproximacion - n) > precision:
            aproximacion = 0.5 * (aproximacion + n / aproximacion)
        return aproximacion
    '''
    2.Ecuacion de Segundo Grado
    '''
    @staticmethod 
# 2 Resolviendo una ecuación de segundo grado, sin usar el módulo math
# Función para calcular las raíces de una ecuación cuadrática
    def calcular_raices(a, b, c):
     discriminante = b**2 - 4*a*c

     if discriminante > 0:
        raiz1 = (-b + discriminante**0.5) / (2*a)
        raiz2 = (-b - discriminante**0.5) / (2*a)
        return raiz1, raiz2
     elif discriminante == 0:
        raiz_unica = -b / (2*a)
        return raiz_unica
     else:
        # Raíces complejas
        parte_real = -b / (2*a)
        parte_imaginaria = (abs(discriminante)**0.5) / (2*a)
        raiz1 = complex(parte_real, parte_imaginaria)
        raiz2 = complex(parte_real, -parte_imaginaria)
        return raiz1, raiz2

    @staticmethod 
    def ecuNumpy(a,b,c):
        soluciones=np.roots([a,b,c])
        return soluciones
    
  
    '''
    3.Calcular PI
    '''
    @staticmethod 
    def calcular_pi_Math():
        pi = math.pi
        print("El valor de pi es:", pi)

    @staticmethod 
    def calcular_pi_leibniz(n):
        suma = 0
        for i in range(n):
            termino = (-1) ** i / (2 * i + 1)
            suma += termino
        pi_aproximado = 4 * suma
        return pi_aproximado
    '''
    4.Calcular Factorial
    '''
    @staticmethod 
    def calcularFactorialMath(n):
        if n < 0:
            return 
        elif n == 0:
            return 1
        else:
            return math.factorial(n)

    @staticmethod
    def calcularFactorial(n):
        fact = 1
        while n > 0:
            fact *= n
            n -= 1
        return fact
    
    '''
    5.Contar apariciones de un numero
    en una lista
    '''
    @staticmethod
    def contar_apariciones(lista, c):
        contador = 0
        for i in lista:
            if i == c:
                contador += 1
        return contador

    @staticmethod
    def listaAleatorios(n,r):
        lista = [0] * n
        for i in range(n):
            lista[i] = random.randint(1,r)
        return lista
    
    '''
      6.Dos numeros grandes consecutivos de una lista
    '''
    @staticmethod
    def numeros_consecutivos(lista):
        if len(lista) < 2:
             return None

        max1 = max2 = float('-inf')

        for i in range(len(lista) - 1):
            if lista[i] > max1:
                max1 = lista[i]
                max2 = lista[i + 1]

        return max1, max2


    # lista = [2, 5, 7, 9,9, 3, 8, 6,504,504,672,675,14523,5416,125745,1454571,15151515,15151515]
    #lista = [2, 5, 7, 9,9, 3, 8, 6,15,10]
    lista = [2, 5, 7, 9,12,20,45]
    resultado = numeros_consecutivos(lista)
    if resultado:
        print(f"Los dos números más grandes consecutivos son: {resultado[0]} y {resultado[1]}")
    else:
        print("La lista es demasiado corta para encontrar dos números consecutivos.")


    '''
    7.Regresar el indice del predecesor menor de una lista
    de cadenas
    '''
    @staticmethod
    def indice_procesador_menor(lista):
        if not lista:
            return None  # Manejamos el caso de una lista vacía

        menor_longitud = len(lista[0])
        indice_menor = 0

        for i in range(1, len(lista)):
            longitud_actual = len(lista[i])
            if longitud_actual < menor_longitud:
                menor_longitud = longitud_actual
                indice_menor = i
        return indice_menor
    
    @staticmethod
    def obtnerCadena():
        while True:
            cadena = input("Ingresa una cadena: ")
            if cadena.strip():  # Verifica si la cadena no está vacía después de quitar espacios en blanco
                return cadena
            else:
                print("La cadena no puede estar vacía. Inténtalo de nuevo.")
                
    '''
    8. Suma de series
     '''
    '''
     Version 1
     '''
    @staticmethod
    def maxSumaV1(s, n):
         suma = [[0 for _ in range(n)] for _ in range(n)]
         for i in range(n):
             for j in range(i):
                 suma[j][i] = suma[j][i - 1] + s[i]   

             suma[i][i] = s[i]

         max = 0
         for i in range(n):
             for j in range(i):  # Cambiar i-1 a i
                 if suma[j][i] > max:
                     max = suma[j][i]

         return max
    '''
     Version 2
     '''
     
    @staticmethod 
    def maxSumaV2(s, n):
        max = 0
        suma = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(i):
                suma[j][i] = suma[j][i - 1] + s[i]
                if suma[j][i] > max:
                    max = suma[j][i]
            
            suma[i][i] = s[i]
            if suma[i][i] > max:
                max = suma[i][i]

        return max
    
    '''
    Version 3
    '''
    
    @staticmethod 
    def maxSumaV3(s,n):
        max = 0
        suma = 0
        for i in s:
            if suma + i > 0:
                suma += i
            else:
                suma = 0
            if suma > max:
                max = suma
        return max

    @staticmethod
    def nPr(n, r):
        factorial_n = MathSolver.calcularFactorial(n)
        factorial_temp = MathSolver.calcularFactorial(n - r)
        permutacion = factorial_n / factorial_temp
        return permutacion

    @staticmethod
    def nCr(n, r):
        permu = MathSolver.nPr(n, r)
        factorial_n = MathSolver.calcularFactorial(r)
        combinacion = permu / factorial_n
        return combinacion

    @staticmethod
    def generarPermuta(n, r, permuta=[]):
        if len(permuta) == r:
            yield permuta[:]
        else:
            for i in n:
                if i not in permuta:
                    permuta.append(i)
                    yield from MathSolver.generarPermuta(n, r, permuta)
                    permuta.pop()
    @staticmethod  
    def generarPerLibreria(n,r):
        # Genera las permutaciones con la libreria permutations
        permuta=list(permutations(n,r))
        for i in permuta:
            print(i)
        print()
        return permuta
    @staticmethod
    def generarCombina(n, r, combi=[], i=0):
        if len(combi) == r:
            yield combi[:]
            return
        if i == len(n):
            return
        combi.append(n[i])
        yield from MathSolver.generarCombina(n, r, combi, i + 1)
        combi.pop()
        yield from MathSolver.generarCombina(n, r, combi, i + 1)
    @staticmethod 
    def generarCombLibreria(n,r):
        combiL=list(combinations(n,r))
        print(combiL)
    
        
        
        
