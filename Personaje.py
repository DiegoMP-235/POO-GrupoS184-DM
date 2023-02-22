class Personaje:
  
    #Constructor de la clase Personaje
    def __init__(self,especie,nombre,altura):
        self.especie = especie
        self.nombre = nombre
        self.altura = altura
        
     #Metodos del personaje   
    def correr(self,status):
        if(status):
            print("El personaje "+self.nombre+" esta corriendo")
        else:
            print("El personaje "+self.nombre+" esta detenido")    
        
    def lanzarGranada(self):
        print("El personaje "+self.nombre+" lanzo una granda... ")        
    
    def recargarArma(self,municiones):
        cargador=10
        cargador+=municiones
        print("El arma tiene "+str(cargador)+" balas")    