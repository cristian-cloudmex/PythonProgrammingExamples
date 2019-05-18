
# -*- coding: utf-8 -*-
#Ejemplo de compresion de listas 
#Desarrollado por el equipo de CloudMex Analytics

#Este ejemplo consiste en un metodo de simplificar la tarea de crear una lista en base a otra lista 
#de la cual solo requerimos ciertos datos y esos datos requerimos hacerles una modificación

lista = [1,2,3,4,5]

#Manera extendida de resolver el problema
list2 = []

for x in lista:
    if x==5:
        list2.append(x**2)

print (list2)

#Forma eficiente de resolverlo (Compresion de listas)
list3 = [x**2 for x in lista if x==5] 
print(list3)