#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 14:52:19 2023

@author: zekibestia
"""
import sys
from Metodos import Metodos
def imprimir_texto_grande(texto):
    ascii_art = {
        'c': r"""
         _____
        /     
       /      
       \      
        \__\    
        """,
        'y': r"""
        _   _  
       | | | |  
       | | | |  
       | | | |  
       |  ___|  
       | |      
       |_|      
        """,
        'l': r"""
         _      
        | |     
        | |     
        | |     
        | |     
        | |____ 
        |______|
        """,
        'o': r"""
         _____   
        /     \  
       |  0  0  | 
        \  ∆  /  
         \___/   
        """,
        'n': r"""
         _   _  
        | \ | | 
        |  \| | 
        | . ` | 
        | |\  | 
        |_| \_| 
        """,
        'e': r"""
         _____   
        |  ____| 
        | |__    
        |  __|   
        | |____  
        |______| 
        """,
        '4': r"""
        |  4  |
        |  |  |
        |__|__|
        """,
    }


def main():
    # Texto a mostrar en grande
    texto_grande = "cyclone 4"
    
    # Imprimir el texto en grande
    imprimir_texto_grande(texto_grande)

if __name__ == "__main__":
    main()
