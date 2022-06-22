import random
from logging.config import fileConfig

def open_file():
    file = 'test-word.txt'
    print(f'Your file is: {file}')
    with open(file) as open_file:
        read_file = open_file.readlines()
        return read_file

def make_word_list(file):
    word_list=[]
    for line in file:
        for word in line.split():
            word_list.append(word)
    return word_list

def pick_word(file):
    mystery_word = random.choice(file)
    return mystery_word

def make_letter_list(file):
    letter_list=[]
    for letter in file:
        letter_list.append(letter)
    return letter_list

def submit_guess(file):
    user_guess = input('Guess a letter: ')
    if user_guess.isalpha() and len(user_guess) == 1:
        lowercase_guess = user_guess.lower()
        print(f'You guessed {lowercase_guess}')
        return lowercase_guess
    else:
        print(f'That guess wasn\'t valid. Please try again.')
        return submit_guess(file)

def play_game():
    file_opened = open_file()
    new_version = make_word_list(file_opened)
    # print('new', new_version)
    # # prints the list with plain strings
    computer_word = pick_word(new_version)
    print(computer_word)
    # prints the word randomly selected by the pick_word function

    letters_to_guess = make_letter_list(computer_word)
    # print(letters_to_guess)
    # # prints letters of the randomly selected word as a list

    submit_guess(letters_to_guess)
    # allows user to submit a guess

if __name__ == "__main__":
    play_game()