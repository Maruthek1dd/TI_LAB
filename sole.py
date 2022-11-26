# juego matematico
# juego que verifica el resultado de operaciones matematicas (sumas y/o restas)
import random
print("---JUEGO MATEMATICO---\nSUMAS-RESTAS\n3 NIVELES PARA ESCOGER: 1-FACIL\n2-INTERMEDIO\n3-DIFICIL")
print(
    "NIVEL 1: Operaciones con maximo 2 numeros (1 Suma y 1 resta) - Numero maximo admitido=100\nNIVEL 2: Operaciones con maximo 3 numeros (Sumas y/o restas) - Numero maximo adimitido=1500\nNIVEL 3: 2 tipos de operaciones diferentes con con 3 numeros (Suma de 2 numeros y una resta, Resta de 2 numeros y una suma) - Numero maximo admitido=10000")
resultado = 1
while resultado == 1:
    level = int(input("Escoga el nivel correcto: 1-FACIL\n2-INTERMEDIO\n3-DIFICIL "))
    while level != 1 and level != 2 and level != 3:
        level = int(input("eso no es correcto, 1-FACIL\n2-INTERMEDIO\n3-DIFICIL"))
    if level == 1:
        num1 = random.randrange(100)  # el numero va desde el rango [0;100]
        num2 = random.randrange(100)
        print("Cual es el resultado de la siguiente operacion?\n", num1, "+", num2,
              "=...?")  # resultado que ingresa el usuario
        useresult = int(input())
        correctresult = num1 + num2  # resultado correcto = calculo de python
        if useresult == correctresult:
            print("Correcto! Sigues participando del juego!")
            resultado = 1
        else:
            resultado=2

    if level==2:
        num1=random.randrange(1500) #el numero va desde el rango [0;1500]
        num2=random.randrange(1500)
        num3=random.randrange(1500)
        print("Cual es el resultado de la siguiente operacion?\n",num1,"+",num2,"+",num3,"=...?") #resultado que ingresa el usuario
        useresult=int(input())
        correctresult=num1+num2+num3 #resultado correcto = calculo de python
        print("Cual es el resultado de la siguiente operacion?\n",num1,"-",num2,"-",num3,"=...?") #resultado que ingresa el usuario
        useresult2=int(input())
        correctresult2=num1-num2-num3 #resultado correcto = calculo de python
        if useresult==correctresult: #verifico la primer operacion
            if useresult2==correctresult2: #verifico la segunda operacion
                print("Correcto! Sigues participando del juego!") #si todo es OK, entonces se continua
                resultado=1
        else:
            resultado=2
    if level==3:
        num1=random.randrange(10000) #el numero va desde el rango [0;10000]
        num2=random.randrange(10000)
        num3=random.randrange(10000)
        print("Cual es el resultado de la siguiente operacion?\n",num1,"+",num2,"-",num3,"=...?") #resultado que ingresa el usuario
        useresult=int(input())
        correctresult=num1+num2-num3 #resultado correcto = calculo de python
        print("Cual es el resultado de la siguiente operacion?\n",num1,"-",num2,"+",num3,"=...?") #resultado que ingresa el usuario
        useresult2=int(input())
        correctresult2=num1-num2+num3 #resultado correcto = calculo de python
        print("Cual es el resultado de la siguiente operacion?\n",num1,"-",num2,"-",num3,"=...?") #resultado que ingresa el usuario
        useresult3=int(input())
        correctresult3=num1-num2-num3 #resultado correcto = calculo de python
        print("Cual es el resultado de la siguiente operacion?\n",num1,"+",num2,"+",num3,"=...?") #resultado que ingresa el usuario
        useresult4=int(input())
        correctresult4=num1+num2+num3 #resultado correcto = calculo de python
        if useresult==correctresult: #comprobacion de la primer operacion
            if useresult2==correctresult2: #comprobacion de la segunda operacion
                if useresult3==correctresult3: #comprobacion de la tercer operacion
                    if useresult4==correctresult4: #comprobacion de la cuarta operacion
                        print("Correcto! Sigues participando del juego!") #si todo es OK, entonces se continua
                        resultado=1
    else:
        resultado = 2
        print("Perdiste...") #cuando se deja de iterar el ciclo while (mientras) se muestra el mensaje de perdida en el juego
        exec(open("menu.py").read())
