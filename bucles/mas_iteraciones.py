''' MAS ITERACIONES '''
import os
os.system('cls')
frutas = ['banana','manzana','ciruela','pera','naranaja','granada','durazno']
cadena ='Hola Alex'
numeros = [2, 5, 8, 10]
#Saltando un iteracion con el continue bajo una condicion
for fruta in frutas:
    if fruta =='granada':
        continue
    print(   f'Me voy a comer una : {fruta}'  )

#Saliendo del bucle con el break bajo una condicion
for fruta in frutas:
    if fruta =='pera':
        break
    print(   f'Me voy a comer una : {fruta}'  )

print('\n')
for letra in cadena:
    print(letra)

#for en una sola linea de codigo
numeros_duplicados = list()
for numero in numeros:
    numeros_duplicados.append(numero * 2)
print(numeros_duplicados)

# Lo mismo en una linea de codigo
numero_duplicado = [x*2 for x in numeros]
print(numero_duplicado)