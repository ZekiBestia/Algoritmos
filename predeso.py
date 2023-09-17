#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 19:29:01 2023

@author: zekibestia
"""

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

# Ejemplo de uso:
procesadores = ["Intel Core i722", "AMD Ryzen 522", "Intel Core i5", "AMD Ryze2n 32", "Intel Core i931"]
indice_menor = indice_procesador_menor(procesadores)

if indice_menor is not None:
    print(f"El procesador más corto se encuentra en el índice {indice_menor}: {procesadores[indice_menor]}")
else:
    print("La lista de procesadores está vacía.")