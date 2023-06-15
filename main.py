import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
length = len(chosen_word)
print(f'The solution is {chosen_word}.')

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the
# letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

display = []
for i in range(length):
    display += "_"

endgame = False
for item in range(length):
    while not endgame:
        guess = input("Please guess a letter: \n").lower()

        if guess in chosen_word:
            print("Right")
        else:
            print("Wrong")

        for i in range(length):
            if chosen_word[i] == guess:
                display[i] = guess

        if "_" not in display:
            endgame = True
        print(display)