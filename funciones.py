# -*- coding: utf-8 -*-
#Ejemplo de funciones 
#Desarrollado por el equipo de CloudMex Analytics

#crearemos una función que sume 2 numeros
#definimos una función
def sumar(num1,num2):
    suma = num1+num2
    suma ="La suma es: {}".format(suma)
    return suma

num1 = int(raw_input("Introduce un numero: "))
num2 = int(raw_input("Introduce un segundo numero: "))

mensaje = sumar(num1,num2)
print(mensaje)