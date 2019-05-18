# -*- coding: utf-8 -*-
#Ejemplo de utilizacion de la entrada de datos por teclado 

 #almacena el valor entero introducido por el usuario en la variable numero y muestra el texto en pantalla "Introduce un numero: "
numero = int(raw_input("Introduce un numero: ")) 

#Realiza la operacion de multiplicacion con el numero introducido  
multiplicacion = numero*numero
multiplicacion_string = "el numero es: {}".format(multiplicacion)

#Imprime en pantalla el calculo de la multiplicacion
print(multiplicacion_string)

#Lista de metodos de string 

#Ejemplo  2 imprimir nuestro nombre y apellido
nombre = raw_input("Dígame su nombre: ")
apellido = raw_input("Dígame su apellido,{} : ".format(nombre))
print("Me alegro de conocerle, {} {}.".format(nombre,apellido))