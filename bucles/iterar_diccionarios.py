''' RECORRIENDO DICCIONARIOS'''

import os
os.system('cls')

diccionario ={
    'nombre':'Alex',
    'apellido':'Vazquez',
    'subs':'100000'
}

print(diccionario)

#Recorriendo e imprimiendo las claves de diccionarios 
for key in diccionario:
    print(key)


#Recorriendo e imprimiendo las claves y los valores de diccionarios 
for key in diccionario.items():
    print(key)

#Desempaquetando y recorriendo
for clave, valor in diccionario.items():
    print(f'La clave de este diccionario es: {clave} y el valor es: {valor}')
