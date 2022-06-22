import random
from logging.config import fileConfig

def open_file():
    file = 'words.txt'
    # print(f'Your file is: {file}')
    with open(file) as open_file:
        read_file = open_file.readlines()
        return read_file
# reads specified file

def make_word_list(file):
    word_list=[]
    for line in file:
        for word in line.split():
            word_list.append(word)
    return word_list
# converts words in file to a list

def pick_word(file):
    mystery_word = random.choice(file)
    return mystery_word
# randomly picks word from file

def make_letter_list(file):
    letter_list=[]
    for letter in file:
        letter_list.append(letter)
    return letter_list
# converts letters in randomly selected word to a list

def submit_guess():
    user_guess = input('Guess a letter: ')
    return user_guess
# allows user to submit a guess

def track_state(file):
    correct_letters=[]
    incorrect_letters=[]
    display = [(letter.replace(letter, "_")) for letter in file]
    print(display)
    while len(incorrect_letters) < 8:
        letter = submit_guess()
        if letter.isalpha() and len(letter) == 1:
            lowercase_guess = letter.lower()
            # if submitted guess is alphabetic and one character, convert to lowercase
            if lowercase_guess in file:
                correct_letters.append(lowercase_guess)
                print(f'Correct! {lowercase_guess} is in the word.')
                display = [(letter.replace(letter, "_")) if letter not in correct_letters else letter for letter in file]
                print(display)
                # if guess is in file, add to correct letters list and replace underscore in display
                if display == correct_letters:
                    print('You won!')
                    break
                    # if display list matches correct letters list, break loop
            else: 
                print(f'{lowercase_guess} is not in the word.')
                incorrect_letters.append(lowercase_guess)
                # if guess is not in file, add to incorrect letters list
        else:
            print(f'That guess wasn\'t valid. Please try again.')
            # if submitted guess is not alphabetic or one character, tell user
        print(f'Letters already guessed:{incorrect_letters + correct_letters}')
        # print concatenated list of letters already guessed
    print('Game over!')
    # game ends when incorrect guesses is 8

def play_game():
    file_opened = open_file()
    # establishes variable to call open_file function with no argument
    new_version = make_word_list(file_opened)
    # establishes variable to call make_word_list function with previous var as arg
    # print('new', new_version)
    # # prints the list with plain strings
    computer_word = pick_word(new_version)
    # establishes variable to call pick_word function with previous var as arg
    # print(computer_word)
    # # prints the word randomly selected by the pick_word function
    letters_to_guess = make_letter_list(computer_word)
    # establishes variable to call make_letter_list function with previous var as arg
    # print(letters_to_guess)
    # # prints letters of the randomly selected word as a list
    track_state(letters_to_guess)
    # calls track_state function with previous variable as argument

if __name__ == "__main__":
    play_game()