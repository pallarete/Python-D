'''CONDICIONALES'''
import os
os.system('cls')

edad = 16
if edad >=18:
    # accion se ejecuta
    print('puedes pasar')
else:
    print('no puedes pasar')
print('no forma parte de ninguna condicion')

contraseña_almacenada = 'AlexMaestro'
contraseña_escrita = 'AlexMaestro'

if contraseña_almacenada == contraseña_escrita:
    # accion se ejecuta
    print('iniciando sesion')
else:
    print('Contraseña equivocada')

ingreso_mensual = 5000

if ingreso_mensual >10000:
    print('Estas bien de pasta en cualquier parte del mundo')

elif ingreso_mensual > 1000:

    print('estas bien de pasta en latinoamerica')
else:

    print('eres pobre')










