import pyautogui as pag
import random
import time

# def BUSCAR():

#     search = pag.locateCenterOnScreen("buscar.png")
#     pag.moveTo(search[0], search[1], 0,5)
#     pag.leftClick()
#     pag.write("invertir online")
#     pag.keyDown("enter")

#     time.sleep(1)

#     entrar_a_la_pagina = pag.locateCenterOnScreen("encontrar.png")
#     pag.moveTo(entrar_a_la_pagina[0], entrar_a_la_pagina[1], 0,5)
#     pag.leftClick()

#     time.sleep(1)

#     entrar_al_login = pag.locateCenterOnScreen("ingresar1.png")
#     pag.moveTo(entrar_al_login[0], entrar_al_login[1], 0,5)
#     pag.leftClick()

# def INGRESAR():

#     PonerCorreo = pag.locateCenterOnScreen("correo.png")

#     pag.moveTo(PonerCorreo[0], PonerCorreo[1], 0,5)
#     pag.leftClick()
#     pag.write("mateotacconi@gmail.com")

#     time.sleep(1)

#     PonerContrasena = pag.locateCenterOnScreen("password.png")

#     pag.moveTo(PonerContrasena[0], PonerContrasena[1], 0,5)
#     pag.leftClick()
#     pag.write("Tacogol_1")

#     PonerIngresar = pag.locateCenterOnScreen("iniciar.png")
#     pag.moveTo(PonerIngresar[0], PonerIngresar[1], 0,5)
#     pag.leftClick()

# BUSCAR()
# time.sleep(1)
# INGRESAR()

# x = 300
# y = 450
# pag.moveTo(x, y, 0,5)
# galletas = 0
# while input("¿queres seguir?") == "si":
#     galletas = 0
#     while galletas < 5:
#         # pag.moveTo(x, y, 0,5)
#         if pag.locateCenterOnScreen("galleta dorada.png") != None:
#             galleta_dorada = pag.locateCenterOnScreen("galleta dorada.png")
#             pag.moveTo(galleta_dorada[0], galleta_dorada[1], 0,5)
#             pag.leftClick()
#         # else:
#         #     continue
#         # pag.leftClick()
#         # galletas += 1

galleta_dorada = pag.locateCenterOnScreen("galleta dorada.png")
pag.moveTo(galleta_dorada[0], galleta_dorada[1], 0,5)
pag.leftClick()

