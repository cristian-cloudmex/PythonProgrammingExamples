# -*- coding: utf-8 -*-
#Ejemplo con diccionarios utilizando condicionales (if/elif)
#Desarrollado por el equipo de CloudMex Analytics

#Este ejemplo consiste en la creación de un diccionario que contenga los estados de la republica con sus respectivas
#capitales, permitiendolas llamar desde consola 

#Creamos el diccionario "estados_republica"
estados_republica = {'aguascalientes':"Aguascalientes", 'baja california': "Mexicali", 'baja california sur': "La paz",
                    'campeche': "Campeche",'coahuila': "Saltillo", 'colima': "Colima", 'chiapas': "Tuxtla Gutiérrez",
                    'chihuahua': "Chihuahua", 'Ciudad de Mexico': "CDMX", 'durango': "Durango", 'guanajuato': "Guanajuato",
                    'guerrero': "Chilpancingo", 'hidalgo': "Pachuca", 'jalisco': "Guadalajara", 'méxico': "Toluca", 
                    'michoacán': "Morelia", 'morelos': "Cuernavaca",'nayarit': "Tepic", 'nuevo león':"Monterrey", 'oaxaca': "Oaxaca",
                    'puebla': "Puebla", 'querétaro': "Querétaro", 'quintana roo': "Chetumal", 'san luis potosí': "San Luis Potosí",
                    'sinaloa': "Culiacán", 'sonora': "Hermosillo", 'tabasco': "Villahermosa", 'tamaulipas': "Ciudad Victoria",
                    'tlaxcala': "Tlaxcala", 'veracruz': "Xalapa", 'yucatán': "Mérida", 'zacatecas': "Zacatecas"} 

#pedimos al usuario el nombre del estado por teclado 
pedir_estado = input("Ingresa el nombre de un estado de la republica mexicana: ")   

#Se busca el nombre en el diccionario y regresa la capital, de no existir regresa un mensaje de error
capital = estados_republica.get(pedir_estado,"El estado solicitado no existe o esta mal escrito, asegurese de escribir en minusculas")

#Crea un condicional, para asegurarnos que la variable capital contenga la capital del estado y no el mensaje de error
if capital != "El estado solicitado no existe o esta mal escrito, asegurese de escribir en minusculas":
    #imprime la capital del estado solicitado
    print("Su municipio es: {}".format(capital))
else:
    #imprime el mensaje de error
    print(capital)
