# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 05:07:01 2024

@author: USER-PC
"""

# CAESAR CIPHER
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(plain_text, shift_amount, cyph_direction):
    response = ''
    for i in plain_text:
        if i in alphabet:
            p = alphabet.index(i)
            if cyph_direction == 'encode':
                np = p + shift # Use the shift to get the new index
                if np > 25: # When the index exceeds the alphabet list range
                    np = np - 26 # Get the index of the letters that come first
            elif cyph_direction == 'decode':
                np = p - shift # Use the shift to get the new index
                if np < 0: # When the index exceeds the alphabet list range
                    np = np + 26 # Get the index of the letters that come first
            np2 = alphabet[np]  # Find the letter in the new index position
            response += np2 # Append the letter in the new empty string
        else: # If its anything but an alphabet, then just add it in the response
            response += i       
    print(f'The {direction}d text is {response}')

# Initiation of the program

should_loop = True
while should_loop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    ##To check if the shift number is greater than 25
    shifter = False
    while not shifter: ##Creating an infinite loop to prompt for the right value
        shift = int(input("Type the shift number:\n"))
        if shift > 25:
            print('Input a number less than 25')
        else:
            shifter = True # break out of the infinite loop
    ##..............
    ##For the actual program now
    caesar(plain_text=text, shift_amount=shift, cyph_direction=direction) 
    ##Prompting what the user wants to do
    prompt = input('Do you want to repeat? {Y or N)\n')
    if prompt == 'N':
        should_loop = False
        print('Goodbye, thanks for playing')
