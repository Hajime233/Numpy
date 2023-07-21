import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


#Anoto cuánto dinero ofrece cada trabajo

dinero1=200
dinero2=5000
dinero3=5
dinero4=100
dinero5=10

#Anoto cuántas horas por semana para realizar cada trabajo

horas1=20
horas2=50
horas3=96
horas4=120
horas5=200

#Genero una lista de python

lista1 = [dinero1, dinero2, dinero3, dinero4, dinero5]

#Genero un arreglo de numpy

List1=np.array(lista1)
print(List1)



#Calculo el promedio

Average1=np.mean(List1)
print(Average1)




#Ordeno los valores

Sort1=np.sort(List1)
print(Sort1)


#Obtengo los primeros dos elementos en un fragmento
FirstTwo= Sort1[0:2]
print(FirstTwo)



#Obtengo los ultimos dos elementos en otro fragmento
Firstthree= Sort1[3:5]
print(Firstthree)



#Calculo la mediana
Middle=np.median(List1)
print(Middle)


#Grafico

Horasa= [horas1,
horas2,
horas3,
horas4,
horas5]

x=np.array(Horasa)

Y=List1

plt.plot(x,Y)



#plt.show()

#El codigo esta correcto y la linea de Plt.Show esta comentada solo para poder habilitar  el codigo a continuacion 
# y que muestre la imagen sin tardar tanto en procesarla con el VSC

Respond=Image.open("Figure_1.png")
Respond.show()


