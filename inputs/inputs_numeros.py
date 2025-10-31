''' INPUTS NUMEROS '''
import os 
os.system('cls')
#Pido un numero
numero = input('Dame un numero :')

# Operando con el numero.
# Siempre hay que convertir a numero. 
# Los inputs SIEMPRE SON STRING!!
# resultado_entero =int(numero)**2
# print(resultado_entero)

resultado_flotante = float(numero) * 2
print(resultado_flotante)