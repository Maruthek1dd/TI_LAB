import random as rd #para que sea alatoria la palabra
import os #para limpiar la consola
import time

cont=0
palabras=["RED","BLACK","CARDS","HOUSE","YELLOW","SEVEN","DOG","ONE"]


while cont<=3:
    indice=rd.randint(0,len(palabras)-1) #0,1,2,3,4,5,6,7
    word=palabras[indice]
    letrapri=word[0] #R
    letraUlt=word[-1] #d
    n=len(word)-2
    completar=n *" _ "
    pista=letrapri + completar + letraUlt
    print(pista)

    palabraUsuario=input("te animas a ser el GPS de esta palabra: ")
    palabraUsuario=palabraUsuario.upper()
    # cond=palabraUsuario == word
    if(palabraUsuario==word):
        cont+=1
        print("VERY GOOOD!")
        
    
    else:
        (palabraUsuario!=word)
        print("TRY AGAIN! ")
    cont==cont
    


if cont==4:
        print("CONGRATULATION YOU WIN!")

time.sleep(3)
os.system("cls")

# print("¿ganaste?: ",cond)

# palMayus=word.upper()#Red



# print("te animas a intentarlo de nuevo?: ")
# os.system("cls")
# palabras=["RED","BLACK","CARDS","HOUSE","YELLOW","SEVEN","DOG","ONE"]
# indice=rd.randint(0,len(palabras)-1) #0,1,2,3,4,5,6,7
# word=palabras[indice]
# palMayus=word.upper()#Red
# letrapri=palMayus[0] #R
# letraUlt=palMayus[-1] #d
# n=len(palMayus)-2
# completar=n *" _ "
# pista=letrapri + completar + letraUlt
# print(pista)
# palabraUsuario=input("te animas a ser el GPS de esta palabra: ")
# palabraUsuario.upper()
# cond=palabraUsuario == palMayus
# if(palabraUsuario==cond):
#  print("¿ganaste?: ",cond)
# else:
#     palabraUsuario!=cond
# print("intentalo de nuevo: ",cond)
# #print("te animas a buscar la palabra nuevamente?: ",)
# os.system("cls")
# palabras=["RED","BLACK","CARDS","HOUSE","YELLOW","SEVEN","DOG","ONE"]
# indice=rd.randint(0,len(palabras)-1) #0,1,2,3,4,5,6,7
# word=palabras[indice]
# palMayus=word.upper()#Red
# letrapri=palMayus[0] #R
# letraUlt=palMayus[-1] #d
# n=len(palMayus)-2
# completar=n *" _ "
# pista=letrapri + completar + letraUlt
# print(pista)
# palabraUsuario=input("te animas a ser el GPS de esta palabra: ".upper())
# cond=palabraUsuario == palMayus
# if(palabraUsuario==cond):
#  print("¿ganaste?: ",cond)
# else:
#     palabraUsuario!=cond
# print("intentalo de nuevo: ",cond)

