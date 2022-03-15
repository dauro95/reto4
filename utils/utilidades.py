def contar_entregados(array_series,array_juegos):
    
    lista_entregados =[]

    for serie in array_series:
        if serie.isEntregado():
            lista_entregados.append(serie)
    
    for juego in array_juegos:
        if juego.isEntregado():
            lista_entregados.append(juego)
    
    return(lista_entregados)

def maxJuego(array_juegos):

    juego_max =array_juegos[0]
    for juego in array_juegos:
        if juego.compare(juego_max):
            juego_max=juego
    return(juego_max)

def maxSerie(array_series):

    serie_max =array_series[0]
    for serie in array_series:
        if serie.compare(serie_max):
            serie_max=serie
    return(serie_max)
