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
import numpy as np
import math
import random

class Metodos:
    
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
    def contar_apariciones(lista, n):
        contador = 0
        for i in lista:
            if i == n:
                contador += 1
        return contador

    @staticmethod
    def listaAleatorios(n):
        lista = [0] * n
        for i in range(n):
            lista[i] = random.randint(1, 500)
        return lista
    '''
    7.Regresar el indice del predecesor menor de una lista
    de cadenas
    '''
    @staticmethod
    def indice_procesador_menor(lista_procesadores):
        if not lista_procesadores:
            return None  # Manejamos el caso de una lista vacía

        menor_longitud = len(lista_procesadores[0])
        indice_menor = 0

        for i in range(1, len(lista_procesadores)):
            longitud_actual = len(lista_procesadores[i])
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
        factorial_n = Metodos.calcularFactorial(n)
        factorial_temp = Metodos.calcularFactorial(n - r)
        permutacion = factorial_n / factorial_temp
        return permutacion

    @staticmethod
    def nCr(n, r):
        permu = Metodos.nPr(n, r)
        factorial_n = Metodos.calcularFactorial(r)
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
                    yield from Metodos.generarPermuta(n, r, permuta)
                    permuta.pop()

    @staticmethod
    def generarCombina(n, r, combi=[], i=0):
        if len(combi) == r:
            yield combi[:]
            return
        if i == len(n):
            return
        combi.append(n[i])
        yield from Metodos.generarCombina(n, r, combi, i + 1)
        combi.pop()
        yield from Metodos.generarCombina(n, r, combi, i + 1)
