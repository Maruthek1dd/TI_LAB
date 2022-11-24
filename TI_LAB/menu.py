import time


def mostrar_menu(opciones):
    print('Seleccione un juego:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (b := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return b


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Memotest!', accion1),
        '2': ('ConSentidos!', accion2),
        '3': ('OrdenMatematico!', accion3),
        '4': ('Select The W_rd', accion4),
        '5': ('Salir', salir)

    }
    
    nombre=input("Escriba su nombre de usuario: ")
    print(f"Hola! {nombre} vamos a jugar? ")
    time.sleep(2)
    generar_menu(opciones, '4')
    


def accion1():
    print('Has elegido el juego Memotest!')
    exec(open("tpiflor.py").read())


def accion2():
    print('Has elegido el juego ConSenti2!')
    exec(open("sopadeletras7.py").read())
    

def accion3():
    print('Has elegido el juego OrdenMatematico!')
    exec(open("ejeciciojuegosole.py").read())
    
def accion4():
    print('Has elegido el juego Select The W_rd')
    exec(open("juegoyeiyei.py").read())


def salir():
    print('Saliendo')



if __name__ == '__main__':
    menu_principal()