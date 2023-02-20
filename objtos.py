from Personaje import *

#1.-Creamos obejto de la clase Personaje

myPersonaje = Personaje()

#2.-Usar atributos
print("El personaje se llama "+myPersonaje.nombre)
print("El personaje tiene la especie "+myPersonaje.especie)
print("El personaje tiene altura de "+myPersonaje.altura)

#3.-Usamos los metodos
myPersonaje.correr(True)
myPersonaje.lanzarGranada()
myPersonaje.recargarArma(15)
