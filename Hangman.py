import random
from word_list import word_list
from Image import stages, logo
print(logo)

chosen_word = word_list[random.randint(0, len(word_list))]
display = []
for every in chosen_word:
    display.append("_")
print(display)
word_length = len(chosen_word)
# for position in range(word_length):
#     letter = chosen_word[position]
#     #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#     if letter == guess:
#         display[position] = letter
# print(display)
# guess = ""
end_of_game = False
lives = 6
used_char = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    used_char += guess 

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")
    lives -= 1
    print(stages[lives])
    if lives == 0:
        end_of_game = True
        print("You Lose!")
    if "_" not in display:
        end_of_game = True
        print("You Win!")
print(f"The word was{chosen_word}")
