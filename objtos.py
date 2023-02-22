from Personaje import *
#1.-Solicitamos los datos
print("######## Crear heroe #########")
NameH = input("Ingresa el nombre de tu heroe\n->")
EspecieH = input("Ingresa la especie de tu heroe\n->")
AlturaH = float(input("Ingresa la altura de tu heroe\n->"))
RecargaH = int(input("Ingresa las balas que quieres recargar\n->"))

print("######## Crear villano #########")
NameV = input("Ingresa el nombre de tu villano\n->")
EspecieV = input("Ingresa la especie de tu villano\n->")
AlturaV = float(input("Ingresa la altura de tu villano\n->"))
RecargaV = int(input("Ingresa las balas que quieres recargar al villano\n->"))

#2.-Creamos obejto de la clase Personaje

myHeroe = Personaje(EspecieH,NameH,AlturaH)
myVillano = Personaje(EspecieV,NameV,AlturaV)

#3.-Usar atributos
print("######## Stats heroe #########")
print("El personaje se llama "+myHeroe.nombre)
print("El personaje tiene la especie "+myHeroe.especie)
print("El personaje tiene altura de "+str(myHeroe.altura))

myHeroe.correr(True)
myHeroe.lanzarGranada()
myHeroe.recargarArma(RecargaH)

print("######## Stats villano #########")
print("El personaje se llama "+myVillano.nombre)
print("El personaje tiene la especie "+myVillano.especie)
print("El personaje tiene altura de "+str(myVillano.altura))

myVillano.correr(False)
myVillano.lanzarGranada()
myVillano.recargarArma(RecargaV)

