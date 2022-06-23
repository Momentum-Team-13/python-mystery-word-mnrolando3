import random
# from logging.config import fileConfig


def open_doc():
    doc = 'words.txt'
    # print(f'Your doc is: {doc}')
    with open(doc) as open_doc:
        read_doc = open_doc.readlines()
        return read_doc
# reads specified document


def make_word_list(file):
    word_list = []
    for line in file:
        for word in line.split():
            word.lower()
            word_list.append(word)
    return word_list
# converts words in file to a list


def pick_word(file):
    return random.choice(file)
# randomly picks word from file


def make_letter_list(file):
    letter_list = []
    for letter in file:
        letter_list.append(letter)
    return letter_list
# converts letters in randomly selected word to a list


def submit_guess():
    return input('- - - - - - - - - -\nGuess a letter: ')
# allows user to submit a guess


def track_state(file):
    correct_letters = []
    incorrect_letters = []
    display = [(letter.replace(letter, '_')) for letter in file]
    print(display)
    while len(incorrect_letters) < 8:
        user_guess = submit_guess()
        if user_guess.isalpha() and len(user_guess) == 1:
            lowercase_guess = user_guess.lower()
            # if submitted guess is alphabetic and one character
            # converts to lowercase
            if lowercase_guess in file:
                if lowercase_guess not in correct_letters:
                    correct_letters.append(lowercase_guess)
                    print(f'\nCorrect! {lowercase_guess} is in the word.\n')
                    # if guess is in file and not in correct letters already
                    # add to correct letters list and replace in display
                    if display == file:
                        print('\nYou won!')
                        break
                        # if display list matches correct letters list
                        # break loop
                else:
                    print('\nYou already guessed that. Try again.\n')
            else:
                if lowercase_guess not in incorrect_letters:
                    print(f'\n{lowercase_guess} is not in the word. \n')
                    incorrect_letters.append(lowercase_guess)
                    # if guess is not in file
                    # add to incorrect letters list
                else:
                    print('\nYou already guessed that. Try again.\n')
        else:
            print('\nThat guess wasn\'t valid. Please try again.\n')
            # if submitted guess is not alphabetic or one character
            # tell user
        display = [(letter.replace(letter, '_')) if letter not in correct_letters else letter for letter in file]
        print(display)
        print(f'Letters already guessed:{incorrect_letters + correct_letters}\n')
        # print concatenated list of letters already guessed
    print('Game over!')
    # game ends when incorrect guesses is 8


def play_game():
    doc_opened = open_doc()
    # establishes variable to call open_doc function with no argument
    new_version = make_word_list(doc_opened)
    # establishes var to call make_word_list with previous var as arg
    # print('new', new_version)
    # # prints the list with plain strings
    computer_word = pick_word(new_version)
    # establishes var to call pick_word with previous var as arg
    # print(computer_word)
    # # prints the word randomly selected by the pick_word function
    letters_to_guess = make_letter_list(computer_word)
    # establishes var to call make_letter_list with previous var as arg
    # print(letters_to_guess)
    # # prints letters of the randomly selected word as a list
    track_state(letters_to_guess)
    # calls track_state with previous variable as argument


if __name__ == "__main__":
    play_game()