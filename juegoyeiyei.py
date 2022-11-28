import random as rd  # para que sea alatoria la palabra
import os  # para limpiar la consola
import time
cont = 0 # contador
palabras = ["RED", "BLACK", "CARDS", "HOUSE", "YELLOW", "SEVEN", "DOG", "ONE"]
print("hello ")
print("welcome Player, al juego de encontrar las  palabras ocultas!")
print("adivina la palabra que se ve por pantalla  utilizando el lenguaje de ingles")
print("si en algun momento quieres retirarte solo presiona 1")
print("te encuentras Ready?")
print("start!!")
while cont <= 3:
    indice = rd.randint(0, len(palabras) - 1)  # 0,1,2,3,4,5,6,7
    word = palabras[indice]
    letrapri = word[0]  # R
    letraUlt = word[-1]  # d
    n = len(word) - 2
    completar = n * " _ "
    pista = letrapri + completar + letraUlt
    print(pista)
    palabraUsuario = input("te animas a encontrar esta palabra: ")
    palabraUsuario = palabraUsuario.upper()
    # cond=palabraUsuario == word
    if (palabraUsuario == word):
        cont += 1
        print("VERY GOOOD!")
    if (palabraUsuario != word and palabraUsuario != "1"):
        print("TRY AGAIN!")
    if (palabraUsuario == "1"):
        print("volviendo al menu")
        cont = 5
if cont == 4:
    print("CONGRATULATION YOU WIN!")

time.sleep(3)
os.system("cls")
exec(open("menu.py").read())


