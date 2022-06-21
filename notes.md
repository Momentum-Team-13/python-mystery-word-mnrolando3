Create an interactive program
- implement a word-guessing game 
    - game called 'Mystery Word'
        - use asciimatics for title
    - game is text-only interactive game

Choose a random value
- create function
    - function selects a word at random from the list of words in the file `words.txt` 

Read from a file
- game runs on the command-line
    - don't pass in the file name as an argument on the command line
        - open the file yourself in code, using its path
    - program should run when this is run:
        ```py
        python mystery_word.py
        ```

Keep track of state
- computer tells user how many letters are in the secret word
    - create function
        - function gets length of word
        - prints underscore multiplied by length
    - user submits one letter each round
        - not case sensitive
            - function to convert guess to .lower()
        - submitting multiple letters in one guess returns error
        - submitting number or special character returns error
        - submitting an already-guessed letter returns error
        - after receiving error, user can submit another guess
- computer tells user if letter is in secret word
    - displays letters guessed in word
        - create function
            - prints letters guessed that match letters in word with underscores in place of unguessed letters
    - displays remaining spaces in word
    - example: word is BOMBARD and the letters guessed are `a`, `b`, and `d`, the screen should display:
        ```txt
        B _ _ B A _ D
        ```
- user is allowed 8 incorrect guesses
    - computer tells user number of remaining guesses after each letter is submitted
    - computer tells user the word if they run out of guesses
- game ends when word is guesses or when user runs out of guesses



### More features

Once the minimum requirements are in place, implement these features. You may not get to these, and that is ok!

1. Let the user choose a level of difficulty at the beginning of the game.
   Easy mode only has words of 4-6 characters; normal mode only has words of 6-8
   characters; hard mode only has words of 8+ characters.
2. When a game ends, ask the user if they want to play again. The game begins again with a new secret word if they reply positively.
3. Use pipenv to install the [colorama package](https://github.com/tartley/colorama) to add colors to your terminal output. If you want to get really fancy, check out [asciimatics](https://github.com/peterbrittain/asciimatics)!

## 🌶 Spicy Mode

Implement the [evil version of this game](http://nifty.stanford.edu/2011/schwarz-evil-hangman/).
Put it in a new Python program called "demon_words.py".

### Attribution

This lab is based off a similar exercise in MIT's 6.00.1x course.
