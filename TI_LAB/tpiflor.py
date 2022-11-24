#defino los componentes del juego, en este caso textos que se van a mostrar
# por pantalla para que el participante los memorize y luego los ingrese nuevamente
# tambien importo sistem y time para usar las funciones
import os
import time
texto1 = "durante varios dias el leon y el hombre compartieron la cueva"
texto2 = "habia una hoja de papel sobre una mesa, cuando una pluma con negrisima tinta la mancho completa"
contador = 2
# comienza el juego, con una breve presentacion para el jugador
print("Hola jugador hoy vamos a poner a prueba tu memoria, ¿Eres capaz de memorizar todo?")
acepta = str(input("responde con si o no: "))
acepta = acepta.lower()
# ahora vamos a preguntar si quiere jugar o no
# vamos a usar un ciclo para preguntar si se quiere quedar o no
while acepta != "si" and acepta != "no":
    # verificacion
    acepta = str(input("esa no es una respuesta correcta vuelve a intentarlo, si para jugar y no para volver al menu"))
    acepta = acepta.lower()
# si decidio quedarse continuamos explicando el juego
# le damos a elegir la modalidad, cada modalidad tiene un texto diferente
while acepta == "si":
    modalidad = int(input("elije la modalidad 1 facil, 2 dificil"))
    while modalidad != 1 and modalidad != 2:
        modalidad = int(input("eso no es correcto por favor ingresa: 1 para Facil o 2 para dificil"))
        # modalidad facil
    while modalidad == 1:
        print("Memoriza el sig texto, tienes unos segundos: ", texto1)
    # con la funcion time. sleep le damos 20seg para que el texto aparezca en pantalla y luego lo borramos
        time.sleep(10)
    # con la funcion os.sistem(cls) hacemos que se borre la pantalla
        os.system("cls")
        textoingreso = str(input("ahora es tu turno escribe la frase sin las comillas, tienes 3 intentos: "))
        textoingreso= textoingreso.lower()
    # aca abrimos un ciclo para que se repita hasta que acierte y corroborar si acerto o no
        while texto1 != textoingreso and contador != 0:
            textoingreso = str(input("no es correcto, vuelve a intentarlo"))
            textoingreso = textoingreso.lower()
            contador = contador - 1
        if textoingreso == texto1:
            print("¡¡¡Perfecto lo lograste!!!")
            time.sleep(2)
        elif contador == 0 :
            print("lo sentimos perdiste...¡pero puede volver a jugar!")
        break
# modalidad dificil, volvemos a hacer lo mismo que antes
    while modalidad == 2:
        print("Memoriza el sig texto, tienes un minuto: ", texto2)
        time.sleep(10)
        os.system("cls")
        textoingreso = str(input("ahora es tu turno escribe la frase correctamente, tienes 3 intentos"))
        while texto2 != textoingreso.lower() and contador != 0:
            textoingreso = str(input("no es correcto, vuelve a intentarlo"))
            contador = contador - 1
        if textoingreso.lower() == texto2:
            print("¡¡¡Perfecto lo lograste!!!")
            time.sleep(2)
        elif contador == 0 :
            print("lo sentimos perdiste...¡pero puede volver a jugar!")
            time.sleep(2)
        break
    break
exec(open("menu.py").read())
# finaliza el juego
