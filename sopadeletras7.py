import os
import time
sopa=[[" O   I   A   E   J   K   L   O   P   L "],
      [" P   E   L   U   D   O   T   M   M   A "],
      [" W   P   C   V   P   I   U   E   R   O "],
      [" A   G   C   D   P   I   E   K   N   S "],
      [" S   U   H   U   E   Y   O   X   B   O "],
      [" P   A   D   A   S   V   B   P   L   T "],
      [" K   T   L   A   F   S   B   H   A   S "],
      [" P   O   A   A   V   I   S   T   N   E "],
      [" C   A   S   A   D   B   Y   E   C   P "],
      [" K   C   O   R   R   O   H   I   O   A "]] # MATRIZ QUE CONTIENE LA SOPA DE LETRA 

soluciones=["SALADO", "APESTOSO","PELUDO","BLANCO","ROCK"] # PALABRAS A ENCONTRAR EN LA SOPA DE LETRA, NOS SIRVE PARA QUE EL PROGRAMA SEPA SI LA RESPUESTA DEL USUSARIO ES CORRECTA
c=""
b="" # VARIABLE QUE NOS SIRVE PARA SACARLE "" A LOS ELEMENTOS DE LA MATRIZ
matriz=[] # NUEVA MATRIZ PARA PASAR EL CONTENIDO DE LA ANTERIOR
cont=0 # CONTADOR PARA QUE EL PROGRAMA SEPA LA SITUACION EN EL JUEGO DEL JUGADOR

def borrarconsola():
 os.system("cls")


print("Hola! vamos a jugar al sopa de letras, estas listo?")
acepta = str(input("responde con si o no: "))
acepta = acepta.upper()
while acepta!="SI" and acepta!="NO":
    acepta = str(input("esa no es una respuesta correcta vuelve a intentarlo"))
while acepta == "NO":
    print("¿quieres salir del juego?, presiona 1 para salir o 2 para quedarte")
    salir = int(input())
    while salir != 1 and salir != 2:
        print("ese valor no es correcto, ingresa 1 para salir o 2 para quedarte")
        salir = int(input())
    if salir == 1:
        print("volver al menu")
    elif salir == 2:
        break

for i in range(1):
    for k in range(10):
            matriz.append(sopa)
            b+=str(matriz[i][k]) + '\n' 
c+=str(b +'\t')
# SEGUNDA MATRIZ
print(" ¡Bienvenido a la sopa de letras!\n")
print("El objetivo es encontrar 5 palabras  relacionadas a los 5 sentidos que tenemos, vamos!!!  ") # CONSIGNA
time.sleep(3)
print(c,'\n') # SE MUESTRA EN PANTALLA LA MATRIZ

while cont<=4:
    RTA=str(input("que palabra encontraste?: ")) 
    RTA=RTA.upper()
    if RTA in soluciones:
        print("respuesta correcta!")
        cont+=1
    else:print("repuesta incorrecta, intenta de nuevo: ")
# CICLO QUE NOS PERMITE ENTRAR LAS RESPUESTAS Y SABER SI ESTAN CORRECTAS O NO
if cont == 5:
    print("FELICITACIONES GANASTE")
time.sleep(3)
os.system("cls")

exec(open("menu.py").read())