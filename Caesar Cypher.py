# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 05:07:01 2024

@author: USER-PC
"""

#Function trials
def greet_with_name(name, location):
    print('Hello', name)
    print('What is the weather like in', location)
##Call the function
greet_with_name("Kotkot", "Bristol")

def greet_with_name(name, location):
    print('Hello', name)
    print('What is the weather like in', location)
##Call the function
greet_with_name(location = "Bristol", name = 'Kots')

##Paint Area calculation
import math
def paint_coverage(height, width, cover):
    number_of_cans = math.ceil(height * width / cover)
    print('You will need', number_of_cans,'cans of paint')
##Input the arguments
test_h = int(input('What is the height?\n'))
test_w = int(input('What is the width?\n'))
coverage = 5
paint_coverage(height = test_h, width = test_w, cover = coverage)

##Prime Number checker
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print('The number is a prime number')
    else:
        print('The number is not prime')
##Call the function
n = int(input('Please give the number:\n'))
prime_checker(number = n)
        
##CAESAR CIPHER
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
##Creating an encryption function
def encrypt(plain_text, shift_amount):
    response = ''
    for i in plain_text:
        p = alphabet.index(i) ##Find the index of the letter in the alphabet
        np = p + shift ##Use the shift to get the new index
        if np > 25: ##When the index exceeds the alphabet list range
            np = np - 26 ##Get the index of the letters that come first
        np2 = alphabet[np]  ##Find the letter in the new index position
        response += np2 ##Append the letter in the new empty string
    print('The encoded text is', response)
##Creating a decryption function
def decrypt(cypher_text, shift_amount):
    response = ''
    for i in cypher_text:
        p = alphabet.index(i) ##Find the index of the letter in the alphabet
        np = p - shift ##Use the shift to get the new index
        if np < 0: ##When the index exceeds the alphabet list range
            np = np + 26 ##Get the index of the letters that come first
        np2 = alphabet[np]  ##Find the letter in the new index position
        response += np2 ##Append the letter in the new empty string
    print('The decoded text is', response)    

##Now to call the functions
if direction == 'encode':
    encrypt(plain_text=text, shift_amount=shift)
elif direction == 'decode':
    decrypt(cypher_text=text, shift_amount=shift)
    
##COMBINED CAESAR Function----This code could be improved by also ciphering characters such as !,? and etc.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(plain_text, shift_amount, cyph_direction):
    response = ''
    for i in plain_text:
        ##The if and elif part of the code below should not affect the ciphered code..
        if i == ' ':##Check if there is an empty space in the string
            response += ' '
            continue
        elif i.isdigit():##Check if there is a number in the string
            response += i
            continue
        else:
            p = alphabet.index(i)
            if cyph_direction == 'encode':
                np = p + shift ##Use the shift to get the new index
                if np > 25: ##When the index exceeds the alphabet list range
                    np = np - 26 ##Get the index of the letters that come first
            elif cyph_direction == 'decode':
                np = p - shift ##Use the shift to get the new index
                if np < 0: ##When the index exceeds the alphabet list range
                    np = np + 26 ##Get the index of the letters that come first
            np2 = alphabet[np]  ##Find the letter in the new index position
            response += np2 ##Append the letter in the new empty string
    print(f'The {direction}d text is {response}')
##Initiation of the program
#from Caesar_logo import logo
#print(logo)    
##Now for the user inputs
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
##To check if the shift number is greater than 25
shifter = False
while not shifter: ##Creating an infinite loop to prompt for the right value
    shift = int(input("Type the shift number:\n"))
    if shift > 25:
        print('Input a number less than 25')
    else:
        shifter = True ##break out of the infinite loop
##..............
##For the actual program now
caesar(plain_text=text, shift_amount=shift, cyph_direction=direction)    

##IMPROVEMENT IN THE CAESAR CIPHER
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(plain_text, shift_amount, cyph_direction):
    response = ''
    for i in plain_text:
        if i in alphabet:
            p = alphabet.index(i)
            if cyph_direction == 'encode':
                np = p + shift ##Use the shift to get the new index
                if np > 25: ##When the index exceeds the alphabet list range
                    np = np - 26 ##Get the index of the letters that come first
            elif cyph_direction == 'decode':
                np = p - shift ##Use the shift to get the new index
                if np < 0: ##When the index exceeds the alphabet list range
                    np = np + 26 ##Get the index of the letters that come first
            np2 = alphabet[np]  ##Find the letter in the new index position
            response += np2 ##Append the letter in the new empty string
        else: ##If its anything but an alphabet, then just add it in the response
            response += i       
    print(f'The {direction}d text is {response}')
##Initiation of the program
#from Caesar_logo import logo
#print(logo)    
##Now for the user inputs
##Check for continuation
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
            shifter = True ##break out of the infinite loop
    ##..............
    ##For the actual program now
    caesar(plain_text=text, shift_amount=shift, cyph_direction=direction) 
    ##Prompting what the user wants to do
    prompt = input('Do you want to repeat? {Y or N)\n')
    if prompt == 'N':
        should_loop = False
        print('Goodbye, thanks for playing')