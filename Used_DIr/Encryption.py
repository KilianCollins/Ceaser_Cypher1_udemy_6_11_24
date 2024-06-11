import math
import random
import numpy


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower().strip(" ")
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(text, shift):
    text_list = []
    index_list = []
    num = 0
    # convertes str into iterable lista
    for let in text:
        text_list += let
    # print(text_list)

    for char in alphabet:
        i = 0
        for char_pos in range(0, len(alphabet)-1):
            if char in text_list and len(text_list) <=i:
                i +=1
                index_list += char_pos
                print(index_list)


    for pos in range(0, len(text_list) -1):
        text_list[pos] = alphabet[index_list[pos]]

    print(text_list)


# for letter in alphabet:
#     if letter in text_list:
#         alphabet[]

encrypt(text,shift)




    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
