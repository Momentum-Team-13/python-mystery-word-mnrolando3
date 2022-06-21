import random
from logging.config import fileConfig

word_list = []

def make_word_list(file):
    for line in file:
        for word in line.split():
            word_list.append(word)
    return word_list

def pick_word(file):
    mystery_word = random.choice(word_list)
    return mystery_word

# def make_letter_list(file):
#     letter_list=[]

#     for letter in mystery_word:
        
#     return letter_list

# def submit_guess():
#   user_guess = input('Guess a letter: ')
#   # get user's guess as a string
#     lowercase_guess = user_guess.lower()
#   if type(user_guess) == str
#     print('Thanks for guessing')
#     #check if the user's guess is a string


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

if __name__ == "__main__":
    file = 'test-word.txt'
    play_game(file)