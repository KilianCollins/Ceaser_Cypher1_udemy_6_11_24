


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower().strip(" ")
shift = int(input("Type the shift number, must be less than ten:\n"))


# my attempt at condesning the code
def ceaser_cypher(plain_text, shift_amount, direction_input):
    if direction_input == "encode":
        cypher_output = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cypher_output += new_letter
        print(cypher_output)
    elif direction_input == "decode":
        cypher_output = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            new_letter = alphabet[new_position]
            cypher_output += new_letter
        print(cypher_output)

# ceaser_cypher(shift_amount=shift, plain_text=text, direction_input=direction)


# instructers way of condesing two overlapping functions into one succinct function

def ceaser(plain_text,shift_amount,cypher_directon):
    end_text = ""
    if cypher_directon == "decode":
        shift_amount = shift_amount * -1
    for letter in plain_text:
        postion = alphabet.index(letter)
        new_position = postion + shift_amount
        end_text += alphabet[new_position]
    print(f"The {cypher_directon}d text is {end_text}") #this is so cool!

ceaser(plain_text=text,shift_amount=shift,cypher_directon=direction)


def encrypt(plain_text, shift_amount):
    # convertes str into iterable list
    cypher_output = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cypher_output += new_letter
    # print(cypher_output)

def decrypt(plain_text, shift_amount):
    cypher_output = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        cypher_output += new_letter
    # print(cypher_output)
#
# if direction == "encode":
#     encrypt(shift_amount=shift,plain_text=text)
#
# elif direction == "decode":
#     decrypt(shift_amount=shift,plain_text=text)
