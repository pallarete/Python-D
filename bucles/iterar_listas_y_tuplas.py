''' ITERANDO LISTAS '''
import os
os.system('cls')

animals = list(['gato', 'perro','loro','cocodrilo'])

numeros = [52, 16, 14, 72]

print(animals)
# Recorriendo la lista animales
for animal in animals:
    print(f'la variable animal es igual a: {animal}')

# Recorriendo y multiplicando cada valor por 10
for numero in numeros:
    resultado = numero * 10
    print (resultado)

# Recorriendo dos listas a la vez
for numero, animal in zip(numeros, animals):
    print(f'Recorriendo lista de numeros: {numero}')
    print(f'Recorriendo lista de animales: {animal}')

# En los rangos no imprime el ultimo dato indicado.
for num in range(5, 10):
    print(num)

print('')

#Forma no optima de recorrer una lista
for num in range(len(numeros)):
    print(numeros[num])

#Forma correcta de recorrer una lista
for num in enumerate(numeros):
    print(type(num))
    print(num)
 
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'El indice es: {indice} y el valor es: {valor}')

for indice, valor in enumerate(numeros):
    print(f'El índice es: {indice} y el valor es: {valor}')

# Usando el else
for numero in numeros:
    print(f' Ejecutando el ultimo bucle, valor actual: {numero}')
else:
    print('El bucle termino')