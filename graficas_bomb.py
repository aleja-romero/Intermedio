import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

datos = pd.read_excel('doble_rendija_datos_bombillo.xlsx')

x_sencilla_uno= datos['distancia 1']
y_sencilla_uno= datos['voltaje 1']

x_sencilla_dos= datos['distancia 2']
y_sencilla_dos= datos['voltaje 2']

x_doble= datos['distancia 3']
y_doble= datos['voltaje 3']

plt.figure(figsize=(10, 6))  
plt.plot(x_sencilla_uno, y_sencilla_uno, marker='o', linestyle='-', color='m', label='Doble')
plt.xlabel('Distancia en micrómetros')
plt.ylabel('Voltaje')
plt.title('Gráfico de sencilla 1 vs Voltaje')

plt.figure(figsize=(10, 6))  
plt.plot(x_sencilla_dos, y_sencilla_dos, marker='o', linestyle='-', color='c', label='Doble')
plt.xlabel('Distancia en micrómetros')
plt.ylabel('Voltaje')
plt.title('Gráfico de sencilla 2 vs Voltaje')

plt.figure(figsize=(10, 6))  
plt.plot(x_doble, y_doble, marker='o', linestyle='-', color='k', label='Doble')
plt.xlabel('Distancia en micrómetros')
plt.ylabel('Voltaje')
plt.title('Gráfico de doble vs Voltaje')



plt.grid(True)
plt.show()



