alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
from logo import logo

print(logo)

# print(chars)


# x = alphabet.index(chars[0])
# print(x)
# shift_f = x + shift
# def ceasar():
#     if direction == "encode":
#         encrypt(plain_text=text, shift_amount=shift)
#     elif direction == "decode":
#         decrypt(coded_text=text, shift_amount=shift)
#
#
# def encrypt(plain_text, shift_amount):
#     encoded = ""
#     for letter in plain_text:
#         place = alphabet.index(letter)
#         # print(place)
#         new_place = place + shift_amount
#         new_letter = alphabet[new_place]
#         encoded += new_letter
#     print(f"The encoded text is {encoded}")
#
#
# def decrypt(coded_text, shift_amount):
#     decoded = ""
#     for letter in coded_text:
#         place = alphabet.index(letter)
#         new_place = place - shift_amount
#         new_letter = alphabet[new_place]
#         decoded += new_letter
#     print(f"The decoded text is {decoded}")


# ceasar(text, shift, direction)

should_continue = True


# decrypt(coded_text=text, shift_amount=shift)
# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(coded_text=text, shift_amount=shift)

def ceaser(in_put, shift_amount, side):
    out_put = ""
    if shift_amount > 26:
        shift_amount %= 26

    if side == "decode":
        shift_amount *= -1

    for letter in in_put:
        if letter in alphabet:
            place = alphabet.index(letter)
            new_place = place + shift_amount
            new_letter = alphabet[new_place]
            out_put += new_letter
        else:
            out_put += letter
    print(out_put)
    cont = input("Do you want to play again? Type 'yes' if you do. ")
    if cont == "yes":
        should_continue = True


while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # chars = list(text)
    chars = list(text)
    ceaser(in_put=text, shift_amount=shift, side=direction)
