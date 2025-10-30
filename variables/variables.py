'''VARIABLES'''
import os
os.system('cls')
print('VARIABLES')
'''LAS VARIABLES SE PUEDEN MODIFICAR'''
#Definiendo una variable
nombre = 'Alex'
#Definiendo una variable con snake_case
nombre_del_tio_mas_guapo = 'Manolo'
nombre = 'Pepe'
print(nombre)

numero = 5
print(numero)
numero = 10
print(numero)

''' Concatenacion de cadenas y variables '''
''' Con la f convierte el dato a texto '''
nombre ='Alex'
bienvenida = f'Hola ' + nombre + ' Como estas?'
print(bienvenida)

nombre ='Alex'
bienvenida = f'Hola {nombre} Como estas?'
print(bienvenida)

nombre = True
bienvenida = f'Hola {nombre} Como estas?'
print(bienvenida)

nombre = 5
bienvenida = f'Hola {nombre} Como estas?'
print(bienvenida)

'''Para borrar una variable (datos alojados en memoria)'''
# del bienvenida

print(bienvenida)

'''Operadores de pertenencia (in, not in) '''
print ('Hola' in bienvenida) # imprime si existe (booleano)
print ('hola' not in bienvenida) # imprime si no existe (booleano)
print ('pedro' in bienvenida) # imprime si existe (booleano)
print ('pedro' not in bienvenida) # imprime si no existe (booleano)


