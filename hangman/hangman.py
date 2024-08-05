from hangman_human import HANGMANPICS
import random

print(HANGMANPICS[0])

WORDS = ("amir","saeed","mohsen","reza","kian")

word = random.choice(WORDS)


correctLetters = ""

guesses = 0

while guesses != 5:

    print("The length of the word is", len(word))

    list_word = list(word)

    letter = input("Guess a letter: ")

    if letter.lower() in word:

        print("Well done", letter, "is in the word")

        correctLetters += letter

        guess_part = ""

        for word_letter in list_word:

            if word_letter in correctLetters:

                guess_part += word_letter

            else:

                guess_part += " - "
                
        print("Correctly guessed letters are: ", guess_part)
    else:

        print("No", letter, "is not in the word")

        correctLetters += "-"
        print(HANGMANPICS[guesses])
        guesses += 1
        


guess = input("Please now guess a word that it could be!: ")

if guess == word:

    print("Well done, you guessed it")

    input("\n\nPress enter key to exit")

else:
    
    ("You did not guess it, the word was: ",word)