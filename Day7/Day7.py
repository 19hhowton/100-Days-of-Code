from hangman_words import word_list
import hangman_art
import random
import replit

print(hangman_art.logo)

chosen_word = random.choice(word_list)
print(chosen_word)

display = ["_" for i in chosen_word]

lives = 6
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    replit.clear()
    correct_guess = False

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
            correct_guess = True

    print(' '.join([i for i in display]))

    if not correct_guess:
        lives -= 1
        if lives == 0:
            print("No more lives. You lose.")
            end_of_game = True #!#
        else:
            print(f"{guess} is not in the word. You have {lives} lives left.")

    print(list(hangman_art.stages)[lives])

    if "_" not in display:
        end_of_game = True
        print("You win.")
