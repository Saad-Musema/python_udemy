alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
# chars = list(text)
chars = list(text)


# print(chars)


# x = alphabet.index(chars[0])
# print(x)
# shift_f = x + shift
def ceasar():
    if direction == "encode":
        encrypt(plain_text=text, shift_amount=shift)
    elif direction == "decode":
        decrypt(coded_text=text, shift_amount=shift)


def encrypt(plain_text, shift_amount):
    encoded = ""
    for letter in plain_text:
        place = alphabet.index(letter)
        # print(place)
        new_place = place + shift_amount
        new_letter = alphabet[new_place]
        encoded += new_letter
    print(f"The encoded text is {encoded}")


def decrypt(coded_text, shift_amount):
    decoded = ""
    for letter in coded_text:
        place = alphabet.index(letter)
        new_place = place - shift_amount
        new_letter = alphabet[new_place]
        decoded += new_letter
    print(f"The decoded text is {decoded}")


ceasar(text, shift, direction)
# decrypt(coded_text=text, shift_amount=shift)
# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(coded_text=text, shift_amount=shift)


