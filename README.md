
#🎮 Python Based Hangman Game

This project implements a classic Hangman word-guessing game using Python.
The player must guess the hidden word one letter at a time. Each incorrect guess draws a new part of the hangman. The game ends when the word is guessed correctly or all chances are used.

📦 Word Guessing Logic

The game randomly selects a word from a predefined list and displays it as blanks.
The player inputs one letter per turn, and the program checks:

✔ If the letter exists in the word → letter is revealed

❌ If the letter is wrong → number of tries decreases and hangman drawing progresses

⛔ Repeated or invalid inputs are blocked

🎉 Player wins if all letters are revealed before tries run out

🔧 Program Components
Component	Description
get_random_word()	Selects a random word from the word list
display_word()	Shows correct guessed letters and underscores
display_hangman()	ASCII art stages of hangman drawing
play_hangman()	Main game loop handling guesses, tries, and win/lose logic
hangman.py	The complete Python implementation
🧠 Working Principle
1️⃣ Word Selection

A random word is chosen from:
['python', 'jupyter', 'notebook', 'hangman', 'programming', 'developer']

2️⃣ Displaying Progress

Correct letters are revealed, incorrect ones reduce tries.

3️⃣ ASCII Hangman Drawing

Each wrong guess displays a new stage of the hangman:

Head

Body

Arms

Legs

4️⃣ Win/Lose Condition

If all letters are guessed → You Win! 🎉

If tries reach zero → Game Over!

📂 Project Structure
File	Description
hangman.py	The complete Python game code
README.md	Documentation file
📝 Python Code Summary

The script performs the following:

Chooses a word at random

Repeatedly asks the player for a single-letter guess

Tracks guessed and incorrect letters

Updates hangman ASCII drawing after each wrong guess

Ends game upon win or failure

🧪 Sample Logic Table
Condition	Action
Letter in word	Reveal letter(s)
Letter NOT in word	Reduce tries, update hangman
All letters guessed	Declare victory
Tries = 0	Game over
🖥 Sample Output (CLI)
Welcome to Hangman!

   ------
   |    |
   |    O
   |
   |
   -
_ _ _ _ _ _
Tries remaining: 6
Guess a letter:

🚀 Future Enhancements

Add GUI using Tkinter

Add category-based words (Animals, Movies, Countries)

Add score or timer system

Load words from external .txt file

Multiplayer mode

Store guess history to track performance

👩‍💻 Author

Developed by HARSHITHA ARUNACHALA
Undergraduate Student, B.E. Electronics and Communication Engineering (ECE)

GitHub: @HARSHITHA292003
