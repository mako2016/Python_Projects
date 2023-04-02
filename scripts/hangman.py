import random
import os
from replit import clear

#clear terminal to start the game
clear()

#using a list to contain 3 word examples for guessing.  
word_list=['hola','python','world']
random_word=random.choice(word_list)


intentos_restantes=len(random_word)
tamanio_palabra=intentos_restantes

display_array=[]

for _ in range(tamanio_palabra):
    display_array.append("_")

while(True):
    clear()

    print(f'Intentos restantes: {intentos_restantes}\n\n')

    print("Estado: \n")
    
    print(f'{random_word}\n')
    print(f'{display_array} \n\n')

    guess=str(input('ingrese una letra: ')).lower()
    intentos_restantes -= 1

    for position in range(len(random_word)):
        #print(f"{position} \n")
    
        if (random_word[position] == guess):
            display_array[position] = guess 

    if("_" not in display_array):
        clear()
        print(display_array)
        print("Adivino la palabra")
        break

    if(intentos_restantes == 0):
        clear()
        print(display_array)
        print('Se acabaron los intentos y no pudo adivinar la palabra')
        break