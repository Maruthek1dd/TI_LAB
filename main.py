# defino los componentes del juego, en este caso textos que se van a mostrar
# por pantalla para que el participante los memorize y luego los ingrese nuevamente
# tambien importo sistem y time para usar las funciones
import os
import time
texto1 = "durante varios dias el leon y el hombre compartieron la cueva"
texto2 = "habia una hoja de papel sobre una mesa, cuando una pluma con negrisima tinta la mancho completa"
contador1 = 3
# comienza el juego, con una breve presentacion para el jugador
print("Hola competidor hoy vamos a jugar con tu memoria, ¿Eres capaz de memorizar todo?")
acepta = str(input("responde con si o no: "))
acepta = acepta.lower()
# ahora vamos a preguntar si quiere jugar o no
# vamos a usar un ciclo para preguntar si se quiere quedar o no
while acepta != "si" and acepta != "no":
# verificacion
    acepta = str(input("esa no es una respuesta correcta vuelve a intentarlo"))
while acepta == "no":
    print("¿quieres salir del juego?, presiona 1 para salir o 2 para quedarte")
    salir = int(input())
    while salir != 1 and salir != 2:
        print("ese valor no es correcto, ingresa 1 para salir o 2 para quedarte")
        salir = int(input())
    if salir == 1:
        print("volver al menu")
    elif salir == 2:
        acepta = "si""
# si decidio quedarse continuamos explicando el juego
# le damos a elegir la modalidad, cada modalidad tiene un texto diferente y guardamos esa eleccion en una variable
modalidad = int(input("elegi la modalidad: 1= Facil, 2 = dificil"))
# usamos un ciclo while para seleccionar las modalidades, luego se explica el texto
while modalidad != 1 and modalidad != 2:
    modalidad = int(input("eso no es correcto por favor ingresa: 1 para Facil o 2 para dificil"))
while modalidad == 1:
# modalidad facil
    print("Memoriza el sig texto, tienes un minuto: Durante varios dias el leon y el hombre compartieron la cueva")
# con la funcion time. sleep le damos un minuto para que el texto aparezca en pantalla y luego lo borramos
# con la funcion os.sistem(cls) hacemos que se borre la pantalla
    time.sleep(60)
    os.system("cls")
    textoingreso = str(input("ahora es tu turno escribe la frase correctamente, tienes 4 intentos: "))
# aca abrimos un ciclo for para darle los intentos al jugador y corroborar si acerto o no
    while corroborartexto1 != textoingreso.lower():
        textoingreso = str(input("no es correcto, vuelve a intentarlo"))
        corroborartexto1 = textoingreso.lower()
        if corroborartexto1 == texto1:
            print("¡¡¡Perfecto lo lograste!!!")
        if corroborartexto1 != textoingreso.lower()
        textoingreso = str(input("no es correcto, vuelve a intentarlo"))
# el contador sirve para luego mostrar el mensaje
        contador1 = contador1 - 1
    if contador1 == 0:
        print("lo sentimos perdiste, pero siempre puedes volver a jugar")
    break
# modalidad dificil, volvemos a hacer lo mismo que antes
while modalidad == 2:
# modalidad dificil
    print("Memoriza el sig texto, tienes un minuto: Habia una hoja de papel sobre una mesa, cuando una pluma con"
          "negrisima tinta la mancho completa")
    time.sleep(60)
    os.system("cls")
    textoingreso = str(input("ahora es tu turno escribe la frase correctamente, tienes 4 intentos"))
    for i in range(0, 3):
        corroborartexto1 = textoingreso.lower()
        if corroborartexto1 == texto2:
            print("¡¡¡Perfecto lo lograste!!!")
            break
        textoingreso = str(input("no es correcto, vuelve a intentarlo"))
        contador1 = contador1-1
    if contador1 == 0:
        print("lo sentimos perdiste, pero siempre puedes volver a jugar")
    break
# finaliza el juego
