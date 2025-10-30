'''Datos complejos/compuestos'''
'''LISTAS. SePueden modificar'''
print('Listas')
import os
os.system('cls')

lista =['Alex Vazquez', "Es guapo",  True, 1.75]
print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(type(lista))

'''TUPLAS. No se pueden modificar'''
print('Tuplas')
tupla =('Alex Vazquez', "Es guapo",  True, 1.75)

print(lista[1])
lista[1] = 'Feo'
print(lista[1])

print(tupla[1])
# tupla[1] = 'Feo' # Esto no se puede hacer en la tupla
print(tupla[1]) # error

''' CONJUNTOS O SETS. Son elementos dedordenados y no siempre
se muestran el el mismo orden. Se puede modificar el conjunto entero
pero no los elementos por separado. No almacena datos duplicados y no se puede
acceder por su indice  '''
# Creando un set o conjunto
conjunto = {'Alex Vazquez', "Es guapo",  True, 1.}
print(conjunto)
conjunto = {'Las mamachico eran putas'}
print(conjunto)

'''DICCIONARIOS'''
'''En los dicts (iguales que los json) hay que llamar al valor por su clave'''
diccionario = {
    'nombre' :'Alex',
    'Canal' : 'Alex',
    'esta emocionado':False,
    'altura':1.75,
    'dato_duplicado':'Alex'
}
print(diccionario['altura'])
print(lista[3])

