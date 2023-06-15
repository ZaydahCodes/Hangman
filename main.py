import random
from hangman_art import stages, logo
from wordlist import word_list

chosen_word = random.choice(word_list)
length = len(chosen_word)
lives = 6
display = []
guess_list = []

print(logo)
print(chosen_word)

for i in range(length):
    display += "_"

endgame = False
for item in range(length):
    while not endgame:
        guess = input("Please guess a letter: \n").lower()
        if guess in guess_list:
            print("This letter has been guessed before,kindly guess another letter.")
        guess_list.append(guess)

        if guess not in chosen_word:
            print(f"The letter '{guess}' is not in the word. You lose a life")
            lives -= 1
            if lives == 0:
                endgame = True
                print("You lose")
            print(stages[lives])

        for i in range(length):
            if chosen_word[i] == guess:
                display[i] = guess
        print(f"{''.join(display)}")
        if "_" not in display:
            endgame = True
            print("You Win")
