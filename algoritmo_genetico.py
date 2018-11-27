from agente import Agente
from tablero import Tablero
from jugar import Jugar
import random as rd
from copy import deepcopy

#Debe tener un N - n agentes
#Debe tener un G - g generaciones
#fitness = total de victorias

class AlgoritmoGenetico:
    poblacion = []

    def __init__(self, tam_poblacion, numero_agentes, numero_generaciones):
        self.iniciar_poblacion(tam_poblacion)
        self.num_agentes = numero_agentes
        self.num_gen = numero_generaciones

    def iniciar_poblacion(self, tam):
        for i in range(tam):
            probabilidad  = self.get_random_caracteristica()
            agente = Agente(probabilidad[0], probabilidad[1], probabilidad[2],probabilidad[3],1)
            self.poblacion+=[agente]

    def get_random_caracteristica(self):
        lista = []
        for i in range(4):
            probabilidad = round(rd.random(),2)
            lista.append(probabilidad)
        return lista
    ''' Debe realizar juego '''
    def juego_genetico(self):

        temporal = self.poblacion[:]
        print(len(temporal))
        for i in range (len(temporal)):
            for j in range (len(temporal)):
                if i!=j:
                    temporal[i], temporal[j] = self.jugar(temporal[i],temporal[j])

        self.poblacion = sorted(temporal[:]  , key=lambda objeto:objeto.victorias, reverse=True)

        for agente in self.poblacion:
            print("victorias= ",agente.get_victorias())
  

    ''' cada generacion se realiza el juego_genetico'''
    def generaciones(self):
        for i in range (self.num_gen):
            self.juego_genetico()
            self.cruce_agentes()
        
    ''' determinacion del ganador'''
    def jugar(self,agente1, agente2):
        
        agente1.set_pieza(1)
        agente2.set_pieza(2)
        juego = Jugar(agente1,agente2)
        return juego.jugar()
    
        

    def print_estrategias(self):
        for a in self.poblacion:
            print(a.get_estrategias())

    def mutacion_cruzado():
        pass


    def cruce_agentes(self):

        poblacion_ordenada = sorted(self.poblacion, key=lambda objeto: objeto.victorias, reverse=True)
        print(len(poblacion_ordenada))
        nueva_poblacion=poblacion_ordenada[:self.num_agentes]
        resto_poblacion=poblacion_ordenada[self.num_agentes:]
        resultado = []
        resultado += nueva_poblacion
        print("res",len(resultado))
        for i in range (len(resto_poblacion)):
            
            if( i==len(resto_poblacion)-1):
                agente = self.mutacion_agente(nueva_poblacion)
                resultado+=[agente]
                break;
                
            else:
                print(i)
                agente = self.cruce_agentes_aux(poblacion_ordenada[i],poblacion_ordenada[i+1])
                resultado.append(agente)
        print(len(resultado))
        self.poblacion = resultado[:]
        
    def cruce_agentes_aux(self, agente1, agente2):
        estrategias1 = agente1.get_estrategias()
        estrategias2 = agente2.get_estrategias()
        nuevo_agente = Agente(estrategias1[0],estrategias2[1], estrategias1[2],estrategias2[3],1)
        return nuevo_agente

    def mutacion_agente(self, poblacion):
        largo = len(poblacion)
        indice = rd.randint(1,largo)-1
        estrategias = poblacion[indice].get_estrategias()
        probabilidad = round(rd.random(),2)
        indice_estrategia = rd.randint(1,4)-1
        estrategias[indice_estrategia] = probabilidad
        agente = Agente(estrategias[0],estrategias[1],estrategias[2],estrategias[3],1)
        return agente
'''
    def cruce_ejemplo(self):
        agente1 = Agente(1,1,1,1,1)
        agente2 = Agente(0,0,0,0,2)
        agente3 = self.cruce_agentes()
        for a in agente3:
            print(a.get_estrategias())
        
'''


alg = AlgoritmoGenetico(4,1,2)
alg.generaciones()

alg.print_estrategias()
    
    
