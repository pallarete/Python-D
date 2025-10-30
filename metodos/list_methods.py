'''METODOS DE LISTAS'''
import os
os.system('cls')

#Funcion de crear una lista
lista = list(['Hola','Alex',45])
print(lista)

# devuelve la cantidad de elementos de una lista al final de una lista
resultado = len(lista)
print(resultado)

#añadiendo elementos al final de la lista. NO se crea una nueva lista
lista.append('jejejej')
print(lista)

#añadiendo elementos en un indice enconcreto
lista.insert(2,'Fuerte')
print(lista)

#añadiedno varios elementos  a la lista. Al final
lista.extend(['chocolate', 'pepinillos'])
print(lista)

print(len(lista))
#elimina el ultimo elemento de la lista o el que queramos pasandole el indice
lista.pop()
print(lista)
print(len(lista))

#elimina un elemento indicando el dato exacto o su valor
lista.remove('jejejej')
print(lista)

#ordenando la lista por orden ascendente solo sin son numeros o booleanos
# lista.sort()
print(lista)

# dandole la vuelta a la lista
lista.reverse()

print(lista)


# Vacia toda la lista
lista.clear()