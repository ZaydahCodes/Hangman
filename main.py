import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
length = len(chosen_word)
lives = 6

print(f'The solution is {chosen_word}.')


display = []
for i in range(length):
    display += "_"

endgame = False
for item in range(length):
    while not endgame:
        guess = input("Please guess a letter: \n").lower()

        if guess not in chosen_word:
            lives -= 1
            if lives == 0:
                endgame = True
                print("You lose")


        for i in range(length):
            if chosen_word[i] == guess:
                display[i] = guess
        print(f"{''.join(display)}")
        if "_" not in display:
            endgame = True
            print("You Win")
        print(stages[lives])
