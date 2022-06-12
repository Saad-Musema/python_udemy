alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
# chars = list(text)
chars = list(text)
print(chars)
# x = alphabet.index(chars[0])
# print(x)
# shift_f = x + shift
for any in range(0, len(chars)):
    place = alphabet.index(chars[any])
    print(place)
    new_place = place + shift
    y = alphabet[new_place]
    print(y)





