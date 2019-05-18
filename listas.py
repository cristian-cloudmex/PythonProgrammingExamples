# -*- coding: utf-8 -*-
#Ejemplo de utilizacion de listas
#Desarrollado por el equipo de CloudMex Analytics

lista1 = [1,2,'nayarit',3.1416]
lista2 = [99, 200,'Jalisco','CloudMex']
print(lista1)
print(lista2)

#añadimos un dato a lista1
lista1.append('hola')
print(lista1)
#Borramos un dato en lista2
lista2.remove('Jalisco')
print(lista2)

#Union de dos listas
lista1.extend(lista2)
print(lista1)

#consultar datos
print(lista1[2])