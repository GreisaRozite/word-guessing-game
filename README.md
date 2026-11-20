# Word Guessing Game

A terminal based word guessing game in Python, inspired by the popular game 'Wordle'

## How to Run

1. Download `wordle.py` and open your terminal in the folder where you saved it
2. Install the following package:
   ```bash
   pip install requests
   ```
4. Run the script:
   ```bash
   python wordle.py
   ```
   
## How to Play
Input one word at a time until you guess the word or run out of attempts. After each guess, the word is returned color coded, where the color of each letter corresponds to its status in the answer:
- `Green` - correct position and letter
- `Yellow` - this letter appears, but in a different position
- `Red` - the answer does not contain this letter at all

## Demo:
<img width="672" height="940" alt="wordle game terminal demo" src="https://github.com/user-attachments/assets/ba47bab0-cef6-4ae9-834c-bd86abc31aa2" />
