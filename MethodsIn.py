#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 11:21:49 2023

@author: zekibestia
"""
import os 
class UserInterface:
 @staticmethod  
 def portada():
     portadas = '''
  ____       ____ _       _   _      _  _   
 / ___|   _ / ___| | ___ | \ | | ___| || |  
| |  | | | | |   | |/ _ \|  \| |/ _ \ || |_ 
| |__| |_| | |___| | (_) | |\  |  __/__   _|
 \____\__, |\____|_|\___/|_| \_|\___|  |_|  
      |___/                               
      '''
     return print(portadas)
        
    
 @staticmethod
 def limpiar_pantalla():
    sistema = os.name
    if sistema == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux
        os.system('clear')
 @staticmethod
 def pedir_numero():
    while True:
        try:
            numero = int(input("Digite el número: "))
            return numero  # Retorna el número si la entrada es válida
        except ValueError:
            print("Error: Debe ingresar un número válido. Inténtelo de nuevo.")
 @staticmethod            
 def pedirABC():
    while True:
        try:
            a = int(input("Digite el número para a : "))# Retorna el número si la entrada es válida
            b= int(input("Digite el número para b : "))
            c = int(input("Digite el número para c: "))
            return a,b,c
        except ValueError:
            print("Error: Debe ingresar un número válido. Inténtelo de nuevo.")
 @staticmethod 
 def pedirListRangeNum():
    while True:
        try:
          n=int(input("Cuantos elementos debe tener la lista: "))
          r=int(input("Rango de 1 a : "))
          c=int(input("Que numero quieres saber sus apariciones: "))
          return n,r,c
        except ValueError:
           print("Debe de elegir un numero valido")
 @staticmethod 
 def pedirNyR():
    while True:
        try:
            entrada = input("Ingrese el conjunto de elementos separados por comas: ")
            n = entrada.split(",")
            n = [int(elem.strip()) for elem in n]
            print("Lista ingresada por el usuario:", n)
            r = int(input("Ingrese el número de elementos que desea tomar del conjunto: "))
            return n, r
        except ValueError:
            print("Error: Asegúrese de ingresar datos válidos.")
 @staticmethod
 def pedirLista():
     entrada = input("Ingrese la lista de elementos separados por comas: ")
     n = entrada.split(",")
     n = [int(elem.strip()) for elem in n]
     return n
        