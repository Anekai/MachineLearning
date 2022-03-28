"""
Created on Mon Mar 28 19:31:04 2022

@author: alexandre.klabunde
"""

from genetic2020 import *

volume_maximo = int(input("Volume máximo: "))
qt_cromossomos = int(input("Cromossomos: "))
qt_geracoes = int(input("Gerações: "))

#[volume, valor]
pacotes = []
qt_pacotes = int(input("Quantidade de pacotes: "))

for i in range(qt_pacotes):
    print()
    print("Pacote " + str(i+1) + "/" + str(qt_pacotes))
    volume = int(input("Volume: "))
    valor = int(input("Valor: "))
    pacotes.append([volume,valor])
    
print()

#EXECUCAO DOS PROCEDIMENTOS
populacao = population(qt_cromossomos, len(pacotes))
historico_de_fitness = [media_fitness(populacao, volume_maximo, pacotes)]
for i in range(qt_geracoes):
    populacao = evolve(populacao, volume_maximo, pacotes, qt_cromossomos)
    historico_de_fitness.append(media_fitness(populacao, volume_maximo, pacotes))

#PRINTS DO TERMINAL
for indice,dados in enumerate(historico_de_fitness):
   print ("Geração: ", indice," | Media de valor no caminhão: ", dados)

print("\nVolume máximo:",volume_maximo,"g\n\nItens disponíveis:")
for indice,i in enumerate(pacotes):
    print("Item ",indice+1,": ",i[0],"m³ | R$",i[1])
    
print("\nExemplos de boas soluções: ")
for i in range(5):
    print(populacao[i])

#GERADOR DE GRAFICO
from matplotlib import pyplot as plt
plt.plot(range(len(historico_de_fitness)), historico_de_fitness)
plt.grid(True, zorder=0)
plt.title("Análise de carga")
plt.xlabel("Geração")
plt.ylabel("Valor médio da carga")
plt.show()