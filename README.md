# Python_Based_Hangman_game
A simple Hangman game implemented in Python. The player guesses letters to find the hidden word, while each wrong guess reveals a new part of the hangman drawing. The game ends when the word is fully guessed or when all attempts are used.

## 🔧 Software Components
| Component | Description |
|----------|-------------|
| Python 3.x | Programming language used |
| random module | Used for selecting random words |
| Terminal / Command Line | Game interface |
| hangman.py | Main game script |

## 🧠 Working Principle

### Word Selection
A random word is selected from a predefined list in the code.

### User Guess Input
The player enters a single letter at a time.

### Decision Making
- Correct letter → revealed in the word  
- Wrong letter → reduces tries + updates hangman drawing  
- All letters guessed → player wins  
- Tries = 0 → game over  

### Hangman Visual
ASCII art stages are displayed based on the number of incorrect guesses.

## 📂 Project Structure
| File | Description |
|------|-------------|
| hangman.py | Python code for the Hangman game |
| README.md | Documentation file |

## 📝 Game Logic Summary
The Python script:
- Selects a random word  
- Tracks guessed & incorrect letters  
- Displays partially guessed word  
- Updates hangman drawing  
- Declares win or loss  

## 🔌 How to Run

Hangman_game.py


## 🚀 Future Enhancements
- Add GUI using Tkinter  
- Category-based word sets  
- Difficulty levels  
- Scoreboard or timer system  

## 👩‍💻 Author
Developed by **HARSHITHA ARUNACHALA**  
Undergraduate Student, B.E. Electronics and Communication Engineering (ECE)  
GitHub: **@HARSHITHA292003**
