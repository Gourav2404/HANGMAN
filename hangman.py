print("This is an simulation of game hangman")
print("LET'S PLAY.........<3 ")

import words_hangman
import random  # Random is a built-in module that you can use to make random Words
import hangman_output_visualss


def hangman():  # Create an function named as hangman
    word_list = words_hangman.words  # Taking words for the words folder
    word = random.choice(word_list)  # Taking random variable
    available_turns = 7  # Number of turns available
    guess_made = ''
    valid_input = set('abcdefghijklmnopqrstuvwxyz')  # Taking set of words

    while (len(word) > 0) is True:
        real_word = ""

        for characters in word:
            if characters in guess_made:
                real_word = real_word + characters

            else:
                real_word = real_word + "_"

        if real_word == word:
            print(real_word)
            print("whooooooo!!!!! Congratulations {} you won the game".format(name))
            break

        print("Guess The Correct Word ", real_word)
        guess = input()

        if guess in valid_input:
            guess_made = guess_made + guess

        else:
            print("Please Enter Correct Characters")
            guess = input()

        if guess not in word:
            available_turns = available_turns - 1

            if available_turns == 6:
                print(" 6 turns left  ")
                print(hangman_output_visualss.HANGMAN_PICS[0])

            if available_turns == 5:
                print(" 5 turns left ")
                print(hangman_output_visualss.HANGMAN_PICS[1])

            if available_turns == 4:
                print(" 4 turns left ")
                print(hangman_output_visualss.HANGMAN_PICS[2])

            if available_turns == 3:
                print(" 3 turns left ")
                print(hangman_output_visualss.HANGMAN_PICS[3])

            if available_turns == 2:
                print(" 2 turns left ")
                print(hangman_output_visualss.HANGMAN_PICS[4])

            if available_turns == 1:
                print(" 1 turns left ")
                print(hangman_output_visualss.HANGMAN_PICS[5])

            if available_turns == 0:
                print(" 0 turns left ")
                print(hangman_output_visualss.HANGMAN_PICS[6])
                print("sorry {} you lost the game better luck next!!\n The word was {}".format(name, word))
                break


name = input("enter your name ")  # Enter your name...
print("welcome {} !".format(name))  # Welcome message
print("-------------------------------------------")
hangman()
