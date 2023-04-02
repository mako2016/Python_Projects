'''
Ceasar encoder / decoder
This Algorithm was made for english texts where there are no ñ o ll.
It will convert input clear text to lower case, but it can be extended to to support case sensitve text.

iam gonna improve the algorithm using a random module to calculate the shift, and a know seed
this makes its better for a man in the middle attack. btw its not robust algorithm to brute force attack.

'''
import random
from replit import clear

def check_numerical_string(string):

    if(string.isdigit()):
        return True
    else:
        return False


def encoder_decoder(shift,encrypt=True):
    
    alphabet_list_original=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ' ]
    counter=1
 
    if (shift == 0): 
        return alphabet_list_original

    if(encrypt):
        alphabet_list_shifted=alphabet_list_original.copy()
        while counter <= shift:
            letter=alphabet_list_shifted.pop(0)
            alphabet_list_shifted.insert(len(alphabet_list_original),letter)
            counter+=1
        
        return alphabet_list_shifted


def encrypt(shift,text):

    alphabet_list_original=encoder_decoder(shift=0)
    alphabet_list_shifted=encoder_decoder(shift,encrypt=True)
    text_list=[]

    for decrypted_letter in text:
        index=alphabet_list_original.index(decrypted_letter)
        text_list.append(alphabet_list_shifted[index]) 
    
    text_encrypted=''.join(text_list)
    
    return text_encrypted


def decrypt(shift,text):

    #define alphabet as string
    alphabet_list_original=encoder_decoder(shift=0)
    alphabet_list_shifted=encoder_decoder(shift,encrypt=True)    
    text_list=[]

    for decrypted_letter in text:
        index=alphabet_list_shifted.index(decrypted_letter)
        text_list.append(alphabet_list_original[index]) 
    
    text_decrypted=''.join(text_list)
    return text_decrypted


#Main body
clear()

mode = str(input('Enter the algorithm mode(encrypt/decrypt): \n'))

if(mode == 'encrypt'):
    seed=random.randint(0,100)
    print(f'La semilla del mensaje es {seed}\n')

    random.seed(seed)
    shift=random.randint(1,1000000)

    clear_text=str(input('Enter clear text: \n')).lower()
    encoded_message=encrypt(shift,clear_text)
    print(f'The encrypted message is {encoded_message}')

elif(mode == 'decrypt'):
    seed=str(input('Enter the decryption seed: \n'))

    if(not check_numerical_string(seed)):
        print('Seed must be an Integer')
    else:
        seed=int(seed)

    random.seed(seed)
    shift=random.randint(1,1000000)

    clear_text=str(input('Enter encrypted text: \n'))
    decoded_message=decrypt(shift,clear_text)
    print(f'The decrypted message is {decoded_message}')
else:
    print('Enter de correct option (encrypt / decrypt)')
