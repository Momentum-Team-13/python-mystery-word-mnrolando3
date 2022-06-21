import random
from logging.config import fileConfig


# def pick_word(file):
#     word_list=[]
#     return random.choice(word_list)

# def submit_guess():
#   user_guess = input('Guess a word: ')
#   # get user's guess as a string
    # lowercase_guess = user_guess.lower()
#   if type(user_guess) == str
#     print('Thanks for guessing')
#     #check if the user's guess is a string
    


def play_game(file):
    print(f'Your file is: {file}')
    with open(file) as open_file:
        read_file = open_file.readlines()

    # computer_word = pick_word(file)
    # print(computer_word)

if __name__ == "__main__":
    file = 'words.txt'
    play_game(file)