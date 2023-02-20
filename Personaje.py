class Personaje:
    especie="Humnano"
    nombre = "Roberto"
    altura = "1.83"
    
#Metodos del personaje

    def correr(self,status):
        if(status):
            print("El personaje "+self.nombre+" esta corriendo")
        else:
            print("El personaje "+self.nombre+" esta detenido")    
        
    def lanzarGranada(self):
        print("El personaje "+self.nombre+" lanzo una granda...")        
    
    def recargarArma(self,municiones):
        cargador=10
        cargador+=municiones
        print("El arma tiene "+str(cargador)+" balas")    