# from enemigos import NaveVerde

def mover_naves(lista,ancho, tamanio_nave,sentido):
    primera = lista[0]
    ultima = lista[len(lista) -1]
    
    #si es de izquierda o derecha
    if(primera.posicion < 0):
        sentido = not(sentido)
    else:
        if(ultima.posicion > ancho-tamanio_nave):
            sentido = not(sentido)

    for nave in lista: 
        nave.mover(sentido)
    return sentido