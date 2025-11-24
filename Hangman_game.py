#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random

# List of possible words for the game
word_list = ['python', 'jupyter', 'notebook', 'hangman', 'programming', 'developer']

# Function to select a random word
def get_random_word(word_list):
    return random.choice(word_list).lower()

# Function to display the current state of the word with guessed letters
def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

# Function to display the hangman based on the number of incorrect guesses
def display_hangman(tries):
    stages = [
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           -
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           -
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |    
           -
        ''',
        '''
           ------
           |    |
           |    O
           |   /|
           |    
           -
        ''',
        '''
           ------
           |    |
           |    O
           |    |
           |    
           -
        ''',
        '''
           ------
           |    |
           |    O
           |    
           |    
           -
        ''',
        '''
           ------
           |    |
           |    
           |    
           |    
           -
        '''
    ]
    return stages[tries]

# Function to run the Hangman game
def play_hangman():
    word = get_random_word(word_list)  # Get a random word from the word list
    guessed_letters = []  # List to store guessed letters
    tries = 6  # Number of attempts (6 tries as per hangman rules)
    word_guessed = False  # Flag to check if the word has been guessed
    
    print("Welcome to Hangman!")
    
    # Game loop
    while not word_guessed and tries > 0:
        print(display_hangman(tries))  # Display the current state of hangman
        print(display_word(word, guessed_letters))  # Display the word with blanks and guessed letters
        print(f"Tries remaining: {tries}")
        
        guess = input("Guess a letter: ").lower()
        
        # Check if input is valid (only single letters)
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter!")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! {guess} is in the word!")
                guessed_letters.append(guess)
                if all(letter in guessed_letters for letter in word):
                    word_guessed = True
        else:
            print("Invalid input. Please enter a single letter.")
    
    # End of game: win or lose
    if word_guessed:
        print(f"Congratulations! You guessed the word '{word}'!")
    else:
        print(display_hangman(tries))
        print(f"Game over! The word was '{word}'.")

# Run the Hangman game
play_hangman()

import random

# List of possible words for the game
word_list = ['python', 'jupyter', 'notebook', 'hangman', 'programming', 'developer']

# Function to select a random word
def get_random_word(word_list):
    return random.choice(word_list).lower()

# Function to display the current state of the word with guessed letters
def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

# Function to display the hangman based on the number of incorrect guesses
def display_hangman(tries):
    stages = [
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           -
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           -
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |    
           -
        ''',
        '''
           ------
           |    |
           |    O
           |   /|
           |    
           -
        ''',
        '''
           ------
           |    |
           |    O
           |    |
           |    
           -
        ''',
        '''
           ------
           |    |
           |    O
           |    
           |    
           -
        ''',
        '''
           ------
           |    |
           |    
           |    
           |    
           -
        '''
    ]
    return stages[tries]

# Function to run the Hangman game
def play_hangman():
    word = get_random_word(word_list)  # Get a random word from the word list
    guessed_letters = []  # List to store guessed letters
    tries = 6  # Number of attempts (6 tries as per hangman rules)
    word_guessed = False  # Flag to check if the word has been guessed
    
    print("Welcome to Hangman!")
    
    # Game loop
    while not word_guessed and tries > 0:
        print(display_hangman(tries))  # Display the current state of hangman
        print(display_word(word, guessed_letters))  # Display the word with blanks and guessed letters
        print(f"Tries remaining: {tries}")
        
        guess = input("Guess a letter: ").lower()
        
        # Check if input is valid (only single letters)
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter!")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! {guess} is in the word!")
                guessed_letters.append(guess)
                if all(letter in guessed_letters for letter in word):
                    word_guessed = True
        else:
            print("Invalid input. Please enter a single letter.")
    
    # End of game: win or lose
    if word_guessed:
        print(f"Congratulations! You guessed the word '{word}'!")
    else:
        print(display_hangman(tries))
        print(f"Game over! The word was '{word}'.")

# Run the Hangman game
play_hangman()

# In[1]:


import random

# List of possible wods for the game
word_list = ['python', 'jupyter', 'notebook', 'hangman', 'programming', 'developer']

# Function to select a random word
def get_random_word(word_list):
    return random.choice(word_list).lower()

# Function to display the current state of the word with guessed letters
def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

# Function to display the hangman based on the number of incorrect guesses
def display_hangman(tries):
    stages = [
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           -
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           -
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |    
           -
        ''',
        '''
           ------
           |    |
           |    O
           |   /|
           |    
           -
        ''',
        '''
           ------
           |    |
           |    O
           |    |
           |    
           -
        ''',
        '''
           ------
           |    |
           |    O
           |    
           |    
           -
        ''',
        '''
           ------
           |    |
           |    
           |    
           |    
           -
        '''
    ]
    return stages[tries]

# Function to run the Hangman game
def play_hangman():
    word = get_random_word(word_list)  # Get a random word from the word list
    guessed_letters = []  # List to store guessed letters
    tries = 6  # Number of attempts (6 tries as per hangman rules)
    word_guessed = False  # Flag to check if the word has been guessed
    
    print("Welcome to Hangman!")
    
    # Game loop
    while not word_guessed and tries > 0:
        print(display_hangman(tries))  # Display the current state of hangman
        print(display_word(word, guessed_letters))  # Display the word with blanks and guessed letters
        print(f"Tries remaining: {tries}")
        
        guess = input("Guess a letter: ").lower()
        
        # Check if input is valid (only single letters)
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter!")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! {guess} is in the word!")
                guessed_letters.append(guess)
                if all(letter in guessed_letters for letter in word):
                    word_guessed = True
        else:
            print("Invalid input. Please enter a single letter.")
    
    # End of game: win or lose
    if word_guessed:
        print(f"Congratulations! You guessed the word '{word}'!")
    else:
        print(display_hangman(tries))
        print(f"Game over! The word was '{word}'.")

# Run the Hangman game
play_hangman()


# In[ ]:


import random

class HangmanGame:
    def __init__(self, word_list):
        self.word_list = word_list
        self.word = random.choice(self.word_list).lower()
        self.guessed_letters = set()
        self.tries = 6

    def display_word(self):
        return ' '.join(letter if letter in self.guessed_letters else '_' for letter in self.word)

    def display_hangman(self):
        stages = [
            """
               ------
               |    |
               |    O
               |   /|\\
               |   / \\
               -
            """,
            """
               ------
               |    |
               |    O
               |   /|\\
               |   / 
               -
            """,
            """
               ------
               |    |
               |    O
               |   /|\\
               |    
               -
            """,
            """
               ------
               |    |
               |    O
               |   /|
               |    
               -
            """,
            """
               ------
               |    |
               |    O
               |    |
               |    
               -
            """,
            """
               ------
               |    |
               |    O
               |    
               |    
               -
            """,
            """
               ------
               |    |
               |    
               |    
               |    
               -
            """
        ]
        return stages[self.tries]

    def play(self):
        print("Welcome to Hangman!")
        while self.tries > 0:
            print(self.display_hangman())
            print(self.display_word())
            print(f"Tries remaining: {self.tries}")
            guess = input("Guess a letter: ").lower()
            
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Enter a single letter.")
                continue
            
            if guess in self.guessed_letters:
                print("You already guessed that letter!")
                continue
            
            self.guessed_letters.add(guess)
            if guess not in self.word:
                print(f"{guess} is not in the word.")
                self.tries -= 1
            elif all(letter in self.guessed_letters for letter in self.word):
                print(f"Congratulations! You guessed the word '{self.word}'!")
                return
        
        print(self.display_hangman())
        print(f"Game over! The word was '{self.word}'.")

if __name__ == "__main__":
    word_list = ['python', 'jupyter', 'notebook', 'hangman', 'programming', 'developer']
    while True:
        game = HangmanGame(word_list)
        game.play()
        if input("Play again? (y/n): ").lower() != 'y':
            break


# In[ ]:


import random

class HangmanGame:
    def __init__(self, word_list):
        self.word_list = word_list
        self.word = random.choice(self.word_list).lower()
        self.guessed_letters = set()
        self.tries = 6

    def display_word(self):
        return ' '.join(letter if letter in self.guessed_letters else '_' for letter in self.word)

    def display_hangman(self):
        stages = [
            """
               ------
               |    |
               |    O
               |   /|\\
               |   / \\
               -
            """,
            """
               ------
               |    |
               |    O
               |   /|\\
               |   / 
               -
            """,
            """
               ------
               |    |
               |    O
               |   /|\\
               |    
               -
            """,
            """
               ------
               |    |
               |    O
               |   /|
               |    
               -
            """,
            """
               ------
               |    |
               |    O
               |    |
               |    
               -
            """,
            """
               ------
               |    |
               |    O
               |    
               |    
               -
            """,
            """
               ------
               |    |
               |    
               |    
               |    
               -
            """
        ]
        return stages[self.tries]

    def play(self):
        print("Welcome to Hangman!")
        while self.tries > 0:
            print(self.display_hangman())
            print(self.display_word())
            print(f"Tries remaining: {self.tries}")
            guess = input("Guess a letter: ").lower()
            
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Enter a single letter.")
                continue
            
            if guess in self.guessed_letters:
                print("You already guessed that letter!")
                continue
            
            self.guessed_letters.add(guess)
            if guess not in self.word:
                print(f"{guess} is not in the word.")
                self.tries -= 1
            elif all(letter in self.guessed_letters for letter in self.word):
                print(f"Congratulations! You guessed the word '{self.word}'!")
                return
        
        print(self.display_hangman())
        print(f"Game over! The word was '{self.word}'.")


def load_words(filename):
    try:
        with open(filename, 'r') as file:
            return [word.strip().lower() for word in file.readlines() if word.strip()]
    except FileNotFoundError:
        print("Word file not found. Using default words.")
        return ['thegooddinosour', 'mufasa', 'findingnemo', 'hangman', 'dopamine', 'stranger']

if __name__ == "__main__":
    word_list = load_words("words.txt")  # Load words from file
    while True:
        game = HangmanGame(word_list)
        game.play()
        if input("Play again? (y/n): ").lower() != 'y':
            break


# In[ ]:




