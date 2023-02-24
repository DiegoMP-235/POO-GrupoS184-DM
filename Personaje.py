class Personaje:
  
    #Constructor de la clase Personaje, definimos los atributos como privados
    def __init__(self,especie,nombre,altura):
        self.__especie = especie
        self.__nombre = nombre
        self.__altura = altura
        
     #Metodos del personaje   
    def correr(self,status):
        if(status):
            print("El personaje "+self.__nombre+" esta corriendo")
        else:
            print("El personaje "+self.__nombre+" esta detenido")    
        
    def lanzarGranada(self):
        print("El personaje "+self.__nombre+" lanzo una granda... ")        
    
    def recargarArma(self,municiones):
        cargador=10
        cargador+=municiones
        print("El arma tiene "+str(cargador)+" balas") 
        
    def __pensar(self):
        print("Estoy pensando...\nI'm thinking")       
        
    #Declaramos los metodos SETTER y GETTER
    def getNombre(self):
        return self.__nombre;
    
    def setNombre(self,nombre):
        self.__nombre = nombre    
        
    def getEspecie(self):
        return self.__especie
    
    def setEspecie(self,especie):
        self.__especie = especie    
        
    def getAltura(self):
        return self.__altura
    
    def setAltura(self,altura):
        self.__altura = altura     