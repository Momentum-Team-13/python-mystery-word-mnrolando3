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

def submit_guess():
    user_guess = input('Guess a letter: ')
    return user_guess

def track_state(file):
    correct_letters=[]
    incorrect_letters=[]
    display = [(letter.replace(letter, "_")) for letter in file]
    print(display)
    while len(incorrect_letters) < 8:
        letter = submit_guess()
        if letter.isalpha() and len(letter) == 1:
            lowercase_guess = letter.lower()
            if lowercase_guess in file:
                correct_letters.append(lowercase_guess)
                print(f'Correct! {lowercase_guess} is in the word.')
                display = [(letter.replace(letter, "_")) if letter not in correct_letters else letter for letter in file]
                print(display)
                if display == correct_letters:
                    print('You won!')
                    break
            else: 
                print(f'{lowercase_guess} is not in the word.')
                incorrect_letters.append(lowercase_guess)
        else:
            print(f'That guess wasn\'t valid. Please try again.')
        print(f'Letters already guessed:{incorrect_letters + correct_letters}')
    print('Game over!')

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
    track_state(letters_to_guess)

if __name__ == "__main__":
    play_game()