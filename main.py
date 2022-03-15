from clases.Serie import Serie
from clases.VideoJuego import VideoJuego
from utils.utilidades import *

    

array_series = [Serie("big bang","comedia","Paul",10),
                Serie("Principe Bel Air","comedia","Tom",10),
                Serie("Equipo A","Accion","Luis",200),
                Serie("LA vida es asi","Infantil","carlos",3),
                Serie("Doraemon","Iinfantil","Luis",5)]


array_juegos = [VideoJuego("call of duty","Accion","EA",200),
                VideoJuego("Super Mario","Aventuras","Nintento",100),
                VideoJuego("Sonic","Aventuras","Sega",1000),
                VideoJuego("FIFA","Deportes","EA",500),
                VideoJuego("F1","Deportes","EA",200)]


array_series[1].entregar()
array_series[4].entregar()
array_juegos[2].entregar()
array_juegos[3].entregar()

lista_entregados = contar_entregados(array_series,array_juegos)


print("\nEl numero de entregados son : " + str(len(lista_entregados)))
print("Se corresponden a : \n")

for entregado in lista_entregados:
    print(entregado)

max_juego= maxJuego(array_juegos)
max_serie = maxSerie(array_series)

print ("------------------------------------\n")
print ("La serie con mas temporadas es:" )
print (max_serie)
print ("------------------------------------\n")
print ("El juego con mas horas es:" )
print(max_juego)

