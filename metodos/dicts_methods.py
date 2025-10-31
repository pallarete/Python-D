''' METODOS DE DICCIONARIOS '''

import os
os.system('cls')

diccionario = {
    'nombre' : 'Alex',
    'apellido' : 'Vazquez',
    'subs': 1000000,
    3 : "Guapo"
}

#Accediendo a una lista de las claves del dict. Sirve para iterar
claves= diccionario.keys()
print(claves)
print('ITEMS')
print(diccionario)
diccionario_iterable =diccionario.items()
print(diccionario_iterable)
print('stop items')

# Accediendo a los valores. 
clave=diccionario.get("kakakakak") #Con el get no dara una excepcion,
# solo nos pasara un None
# clave_para_fallo=diccionario['kakakakak'] asi para la ejecucion
print(clave)

#Esto es una mala practica
clave_num = diccionario[3]
print(diccionario[3])
print(clave_num)

# Eliminando elementos de una lista al reves que en las listas
#  hay que especificar LITERALMENTE EL NOMBRE  una clave
diccionario.pop(3)
print(diccionario)
diccionario.pop('apellido','subs')
print(diccionario)


# Eliminando elementos de una lista (Todos)
diccionario.clear()
print(diccionario)







