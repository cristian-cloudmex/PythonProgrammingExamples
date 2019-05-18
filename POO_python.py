# -*- coding: utf-8 -*-
#Ejemplo de creacion de clases 
#Desarrollado por el equipo de CloudMex Analytics

class Humano:
    #constructor de la clase (inicializa datos)
    def __init__(self):
        self.edad = 20
        self.altura = 1.80
        self.peso = 90

    def hablar(self,edad,altura,peso):
        #creamos atributos y les damos los valores de los parametros que recibe el metodo
        self.edad= edad
        self.altura = altura
        self.peso=peso
        mensaje = "Mi edad es {} años, mido {} y peso {} kg".format(edad,altura,peso)
        print(mensaje) 

#pedimos datos por teclado
edadNueva = int(raw_input("Cual es tu edad?: "))
alturaNueva = float(raw_input("Cual es tu altura?: "))
pesoNueva = int(raw_input("Cual es tu peso?: "))

#creamos un objeto juan basandonos en la clase Humano
juan = Humano()
#mandamos llamar el metodo hablar en donde le pasamos los parametros correspondientes
juan.hablar(edadNueva,alturaNueva,pesoNueva)

