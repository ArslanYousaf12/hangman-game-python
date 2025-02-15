#Step 5

import random
import hangman_words as word
import hangman_art as art

# - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# - Import the logo from hangman_art.py and print it at the start of the game.
print(art.logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You already guess this letter {guess}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word,
        #  print out the letter and let them know it's not in the word.
        print(f"letter is not in choosen word {guess}")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # - Import the stages from hangman_art.py and make this error go away.
    print(art.stages[lives])