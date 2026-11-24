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
   *(Depending on your system, you may need to use `py wordle.py` or `python3 wordle.py` instead.)*
   
## How to Play
Input one word at a time until you guess the word or run out of attempts. After each guess, the word is returned color coded, where the color of each letter corresponds to its status in the answer:
- `Green` - correct position and letter
- `Yellow` - this letter appears, but in a different position
- `Red` - the answer does not contain this letter at all

## Demo:
<img width="1560" height="1136" alt="wordle game terminal demo" src="https://github.com/user-attachments/assets/3b14170f-6866-4a12-a783-448ef0821a73" />
