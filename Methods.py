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
    
    
    def encontrar_numeros_consecutivos(lista, umbral):
     numeros_consecutivos = []

     for i in range(len(lista) - 1):
        if lista[i] > umbral and lista[i + 1] > umbral:
            numeros_consecutivos.append((lista[i], lista[i + 1]))

     return numeros_consecutivos

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
        
    '''
    ??. Encontra el máximo y el mínimo de una lista 
    '''
    def max_minV1():
        n = int(input("Ingrese la cantidad de números en la lista: "))
        lista = []

        for i in range(n):
         num = int(input(f"Ingrese el número {i + 1}: "))
         lista.append(num)

        maximo = lista[0]
        minimo = lista[0]   

        for i in range(1, len(lista)):
            if lista[i] > maximo:
                maximo = lista[i]
            if lista[i] < minimo:
                minimo = lista[i]
        print(f"El número máximo es: {maximo}")
        print(f"El número mínimo es: {minimo}")

    max_minV1()

    '''
    ??. Encontra el valor de la suma maxima de dos valores consecutivos V1
    '''
    def max_sum_consecutive(nums):
    
        max_sum = current_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum += nums[i]
            if current_sum > max_sum:
                max_sum = current_sum
        current_sum -= nums[i-1]
        return max_sum
    input_values = input("Ingrese los valores de la lista separados por espacios: ")
    nums = [int(x) for x in input_values.split()]
    result = max_sum_consecutive(nums)
    print("La suma máxima de elementos consecutivos es:", result)
        
        
