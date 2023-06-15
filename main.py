import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'The solution is {chosen_word}.')

display = []
for i in range(len(chosen_word)):
    display += "_"

guess = input("Please guess a letter: \n").lower()

if guess in chosen_word:
    print("Right")
else:
    print("Wrong")

for i in range(len(display)):
    if chosen_word[i] == guess:
        display[i] = guess

print(display)