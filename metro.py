#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 23:46:37 2023

@author: zekibestia
"""

import pandas as pd
import networkx as nx


datos_nodo=pd.read_csv('metro.csv')
datos_nodo.head()

datos_nodo.set_index("id",inplace=True)
datos_nodo.head()

rutas_nodo=pd.read_csv('resultado.csv')
rutas_nodo.head()

DG=nx.DiGraph()
for filas in rutas_nodo.iterrows():
    DG.add_edge(filas[1]["origen"],
                filas[1]["destino"],
                peso=filas[1]["peso"])
DG.nodes(data=True)

dijkstra=list(nx.dijkstra_path(DG,source="21",target="1",weight="peso"))
print(dijkstra)
datos = datos_nodo.loc["21"]["estacion"]
def ruta(ruta):
    total_peso=0
    for i in range(len(ruta)-1):
        origen=ruta[i]
        destino=ruta[i+1]
        peso=DG[origen][destino]["peso"]
        total_peso=total_peso+peso
        print(" %s->%s\n Peso: %s " % 
              (datos_nodo.loc[origen]['estacion'],
               datos_nodo.loc[destino]['estacion'],peso))
    print("\n Peso total=%s"%(total_peso))

ruta(dijkstra)