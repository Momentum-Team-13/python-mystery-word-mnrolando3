import random
from logging.config import fileConfig

WORD_LIST = []

def make_word_list(file):
    for line in file:
        for word in line.split():
            WORD_LIST.append(word)
    return WORD_LIST

def pick_word(file):
    mystery_word = random.choice(WORD_LIST)
    return mystery_word

def submit_guess():
    user_guess = input('Guess a letter: ')
    if user_guess.isalpha() and len(user_guess) == 1:
        lowercase_guess = user_guess.lower()
        print(f'You guessed {lowercase_guess}')
        return lowercase_guess
    else:
        print(f'That guess wasn\'t valid. Please try again.')
        return submit_guess()

def play_game(file):
    print(f'Your file is: {file}')
    with open(file) as open_file:
        read_file = open_file.readlines()

    new_version = make_word_list(read_file)
    computer_word = pick_word(new_version)
    print(computer_word)

    def make_letter_list(file):
        letter_list=[]
        for letter in computer_word:
            letter_list.append(letter)
        return letter_list

    letters_to_guess = make_letter_list(computer_word)
    print(letters_to_guess)

    submit_guess()

if __name__ == "__main__":
    file = 'test-word.txt'
    play_game(file)