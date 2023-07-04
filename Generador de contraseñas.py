import random
from random import randrange

def CONTRASEÑAS():

    letras_random = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","ñ","z","x","c","v","b","n","m"]
    numeros_random = ["0","1","2","3","4","5","6","7","8","9"]
    signos_random = ["-","_","+"]

    contraseñas_ya_guardadas = []

    leer_UNO = open('contraseñas guardadas.txt','r')
    for line in leer_UNO.readlines():
        contraseñas_ya_guardadas.append(line)
    print(contraseñas_ya_guardadas)
    leer_UNO.close()

    def generar_contra():
        contraseñas = []
        for i in range(8):
            contraseñas += random.choice(letras_random)
            contraseñas += random.choice(numeros_random)
            contraseñas += random.choice(signos_random)
        contraseña_random = contraseñas[0] + contraseñas[1] + contraseñas[2] + contraseñas[3] + contraseñas[4] + contraseñas[5] + contraseñas[6] + contraseñas[7]
        return contraseña_random

    def escribir_contraseña( contraseña_random ):

        para_que_es_la_contraseña = input("¿Para que necesita la contraseña?: ")

        abrir_y_escribir = open('contraseñas generadas.txt','a+')

        agregar_newline = (para_que_es_la_contraseña + '\n')
        contar_repeticiones_de_contraseña = contraseñas_ya_guardadas.count(agregar_newline)
        contar = contraseñas_ya_guardadas.count(para_que_es_la_contraseña)
        
        if (contar_repeticiones_de_contraseña > 0) or (contar > 0):
            print("Ya posee una contraseña para eso")
        else:
            
            abrir_y_escribir.write('\n' + para_que_es_la_contraseña + " Contraseña: " + contraseña_random)
            abrir_y_escribir.close()

            escribir_la_contraseña_en_otro_archivo = open('contraseñas guardadas.txt','a+')
            escribir_la_contraseña_en_otro_archivo.write('\n' + para_que_es_la_contraseña)
            print(contraseñas_ya_guardadas)

            print("Listo, su contraseña es " + contraseña_random + " y se guardo en 'contraseñas generadas.txt'")
    
    escribir_contraseña(generar_contra())

CONTRASEÑAS()
