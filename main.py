def ANAGRAMAS():

    palabras = ["silbar","mocasin","grito","gato","recto","destino","cosa","fresa","marina","mina","polen"]

    # palabras a usar: sentido|frase|iman|saco|pleno|camison|brasil|gota|trigo|corte|animar

    palabra_del_jugador = input("ingrese su palabra: ")

    posicion = 0
    letras_palabra_del_jugador = len(palabra_del_jugador)
    cantidad_maxima_de_letras = 0

    while posicion < 10:

        for letra in palabra_del_jugador:
            if letra in palabras[posicion]:
                cantidad_maxima_de_letras += 1
                if cantidad_maxima_de_letras == letras_palabra_del_jugador:
                    print("|",palabra_del_jugador, "|  -------->  |" ,palabras[posicion],"|")
                    posicion = 10
            elif letra not in palabras[posicion]:
                posicion += 1

def CIFRADO_CESAR():
    
    mensaje_a_cifrar = input("Ingrese el mesnaje a cifrar: ")
    letras_mensaje_cifrado = []
    mensaje_cifrado = " "

    for letra in mensaje_a_cifrar:
        ASCII_letras_cambiadas = ord(letra) + 1
        letras_cambiadas = chr(ASCII_letras_cambiadas)
        letras_mensaje_cifrado.append(letras_cambiadas)
        print(letras_mensaje_cifrado)

    for letra in letras_mensaje_cifrado:
        mensaje_cifrado += letra
        print(mensaje_cifrado)
