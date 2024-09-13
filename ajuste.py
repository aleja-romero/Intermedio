import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

datos = pd.read_excel('datos_laser.xlsx')

x_doble= datos['micro_doble']
y_doble= datos['voltaje_doble']

x_sencilla_una= datos['micro_sencilla_una']
y_sencilla_una= datos['voltaje_sencilla_una'][0:34]

x_sencilla_dos= datos['micro_sencilla_dos']
y_sencilla_dos= datos['voltaje_sencilla_dos'][0:46]

maximo=np.argmax(y_doble)
posicion= y_doble.idxmax()
dts=np.linspace(0,0,len(y_doble))
plt.figure(figsize=(4, 4))

dts[posicion]=0
for i in range((len(y_doble)-maximo)):
    a=posicion+i
    dts[a]=5*i
for i in range(posicion+1):
    dts[posicion-i]=5*(-i)

plt.plot(dts,y_doble,"-")

la=670*(10**(-6))
d=0.356
l=500
a=0.1


I0_a=np.max(y_doble)
I_ab= I0_a * (np.abs(((np.sin((np.pi * a* dts*10**(-2))/(l*la) ))/((np.pi * a * dts*10**(-2))/(l*la)))*np.cos((np.pi*d * dts*10**(-2))/(l*la) )))**2
plt.plot(dts,I_ab,"-")
plt.xlabel('Distancia en micrómetros')
plt.ylabel('Voltaje')
plt.title('Gráfica de doble rendija láser')

plt.grid(True)
plt.errorbar(dts,y_doble, yerr=0.001, fmt='^', ecolor='purple', capsize=5, label='Datos con error')


dts=np.linspace(0,0,len(y_sencilla_una))

posicion1=np.argmax(y_sencilla_una)
dts[posicion1]=0
for i in range((len(y_sencilla_una)-posicion1)):
    dts[posicion1+i]=15*i
for i in range(posicion1+1):
    dts[posicion1-i]=15*(-i)
#plt.subplot(1, 2, 1)

#plt.plot(dts,y_sencilla_una,"-")

I_0=np.max(y_sencilla_una)
la=670*(10**(-6))
d=0.356
l=500
a=0.1
I_1= I_0 * ((np.sin(((np.pi * a * dts*10**(-2))/(l*la))))/((np.pi * a * dts*10**(-2))/(l*la)))**2
#plt.plot(dts,I_1,"-")
#plt.xlabel('Distancia en micrómetros')
#plt.ylabel('Voltaje')
#plt.title('Gráfica de rendija izquierda láser')



dts=np.linspace(0,0,len(y_sencilla_dos))

posicion1=np.argmax(y_sencilla_dos)
dts[posicion1]=0
for i in range((len(y_sencilla_dos)-posicion1)):
    dts[posicion1+i]=15*i
for i in range(posicion1+1):
    dts[posicion1-i]=15*(-i)
plt.subplot(1, 2, 1)

plt.plot(dts,y_sencilla_dos,"-")

I_0=np.max(y_sencilla_dos)
la=670*(10**(-6))
d=0.356
l=500
a=0.1
I_1= I_0 * ((np.sin(((np.pi * a * dts*10**(-2))/(l*la))))/((np.pi * a * dts*10**(-2))/(l*la)))**2
plt.plot(dts,I_1,"-")
plt.xlabel('Distancia en micrómetros')
plt.ylabel('Voltaje')
plt.title('Gráfica de rendija derecha láser')
plt.show()




