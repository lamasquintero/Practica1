#Ejercicio en PYTHON sobre la canción "Bottles of beer on the wall"
##Realizado por Jose Manuel Martínez y Gonzalo Lamas Quintero

# -*- coding: utf-8 -*-

cancion = '''{numeroActual} bottles of beer on the wall, {numeroActual} bottles of beer. Take one down, pass it around, {numeroDecrementado} bottles of beer on the wall.
'''
for botellas in range(99,0,-1):
    print cancion.format(numeroActual=botellas, numeroDecrementado=botellas-1)
