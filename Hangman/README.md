# 🎮 HANGMAN GAME

## 📋 PROJECT DESCRIPTION

This is a classic Hangman game created in Python. The player must guess a word letter by letter before running out of lives. It's a perfect project to practice basic programming concepts such as:
- Loops
- Conditionals (if/elif/else)
- Lists
- Module imports
- String manipulation

---

## 🎯 HOW THE GAME WORKS

### **Rules:**
1. The program chooses a random word from a list
2. The player sees underscores (_) representing each letter
3. The player guesses letters one by one
4. If the letter is in the word → it's revealed in its position
5. If the letter is NOT in the word → the player loses a life
6. The player has **6 lives** in total
7. **Wins** if they guess the entire word before losing all lives
8. **Loses** if they run out of lives before completing the word

### **Game example:**
```
Word to guess: _____
Guess a letter: a
Word to guess: _a___

Guess a letter: e
You guessed 'e', that's not in the word. You lose a life.
5/6 LIVES LEFT
```

---

## 📁 PROJECT STRUCTURE
```
📁 hangman_project/
  ├── hangman.py          ← Main game file (RUN THIS ONE)
  ├── hangman_words.py    ← List of possible words
  └── hangman_art.py      ← Logo and ASCII art drawings of the hangman
```

### **Description of each file:**

#### **1. `hangman.py`** (Main file)
- Contains all the game logic
- Imports words and art from other files
- Handles the main game loop
- Controls lives, wins, and losses

#### **2. `hangman_words.py`**
- Contains the `word_list` with all possible words
- The game chooses a random word from this list
- You can add or remove words as you prefer

#### **3. `hangman_art.py`**
- Contains the game `logo` (title in ASCII art)
- Contains `stages`: a list with 7 hangman drawings
- Each drawing represents a different state (from 6 lives to 0 lives)

---

## 🚀 HOW TO RUN THE GAME

### **Requirements:**
- Python 3.x installed on your computer
- All 3 files must be in the same folder

### **Steps:**

1. **Download or create the 3 files** in the same folder

2. **Open terminal/console** and navigate to that folder:
```bash
   cd path/to/your/folder/hangman_project
```

3. **Run the game:**
```bash
   python hangman.py
```

4. **Play and have fun!** 🎉

---

## 🧠 CODE EXPLANATION (STEP BY STEP)

### **PART 1: Imports and initial setup**
```python
import random
from hangman_words import word_list
from hangman_art import logo, stages

print(logo)  # Displays the game title

lives = 6  # Initial lives
game_over = False  # Controls when the game ends
correct_letters = []  # Correctly guessed letters
guessed_letters = []  # All attempted letters (to avoid repetitions)
```

**What does this do?**
- Imports necessary tools (`random` to choose words randomly)
- Imports data from other files (words and art)
- Initializes game variables

**Why two different lists?**
- `correct_letters`: Only stores letters that ARE in the word (used to build the display)
- `guessed_letters`: Stores ALL attempted letters (prevents trying the same letter twice)

---

### **PART 2: Choose word and create initial display**
```python
chosen_word = random.choice(word_list)  # Chooses a random word
placeholder = "_" * len(chosen_word)  # Creates underscores
print("Word to guess: " + placeholder)
```

**What does this do?**
- `random.choice(word_list)` selects a random word from the list
- `"_" * len(chosen_word)` creates a string with as many underscores as letters in the word
  - Example: if `chosen_word = "python"` (6 letters), then `placeholder = "______"`

**The `*` operator with strings:**
- Repeats a string a specified number of times
- `"a" * 3` → `"aaa"`
- `"_" * 5` → `"_____"`

---

### **PART 3: Main game loop**
```python
while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
```

**What does this do?**
- `while not game_over` means "while the game has NOT ended"
- `not game_over` is the same as `game_over == False`
- The loop continues until `game_over` becomes `True`
- `.lower()` converts everything to lowercase so "A" and "a" are treated the same

---

### **PART 4: Check if letter was already guessed**
```python
if guess in guessed_letters:
    print(f"You've already guessed '{guess}'. Try another letter.")
    continue

guessed_letters.append(guess)
```

**What does this do?**
- Checks if the letter is already in the `guessed_letters` list
- If yes → shows a message and `continue` skips the rest of the loop
- If no → adds the letter to the list with `.append()`

**Why use `continue`?**
- Without it, the code would continue and the player would lose a life unfairly
- `continue` jumps back to the start of the `while` loop immediately

---

### **PART 5: Build the display (what the player sees)**
```python
display = ""

for letter in chosen_word:
    if letter == guess:
        display += letter
        correct_letters.append(guess)
    elif letter in correct_letters:
        display += letter
    else:
        display += "_"

print("Word to guess: " + display)
```

**What does this do?**
This is the heart of the game! Let's see it with an example:

**Example:** Word is `"python"`, player already guessed `"p"` and `"o"`, now tries `"t"`
```python
correct_letters = ["p", "o"]
guess = "t"
display = ""

# Loop through each letter in "python"
for letter in "python":
    
    # Iteration 1: letter = "p"
    # Is "p" == "t"? NO
    # Is "p" in ["p", "o"]? YES
    # Result: display += "p" → display = "p"
    
    # Iteration 2: letter = "y"
    # Is "y" == "t"? NO
    # Is "y" in ["p", "o"]? NO
    # Result: display += "_" → display = "p_"
    
    # Iteration 3: letter = "t"
    # Is "t" == "t"? YES
    # Result: display += "t" and correct_letters.append("t")
    # display = "p_t"
    
    # Iteration 4: letter = "h"
    # Is "h" == "t"? NO
    # Is "h" in ["p", "o"]? NO
    # Result: display += "_" → display = "p_t_"
    
    # Iteration 5: letter = "o"
    # Is "o" == "t"? NO
    # Is "o" in ["p", "o"]? YES
    # Result: display += "o" → display = "p_t_o"
    
    # Iteration 6: letter = "n"
    # Is "n" == "t"? NO
    # Is "n" in ["p", "o"]? NO
    # Result: display += "_" → display = "p_t_o_"

# Final result: "p_t_o_"
```

**The three conditions explained:**
1. `if letter == guess`: The current guess matches this letter → reveal it
2. `elif letter in correct_letters`: This letter was guessed correctly before → show it
3. `else`: This letter hasn't been guessed yet → show underscore

---

### **PART 6: Check if letter is incorrect**
```python
if guess not in chosen_word:
    print(f"You guessed '{guess}', that's not in the word. You lose a life.")
    lives -= 1
    
    if lives == 0:
        game_over = True
        print(f"\n***********************IT WAS '{chosen_word}'! YOU LOSE**********************")
```

**What does this do?**
- `if guess not in chosen_word` checks if the letter is NOT in the secret word
- `lives -= 1` is the same as `lives = lives - 1` (subtracts one life)
- If lives reach 0 → the game ends and shows the correct word

---

### **PART 7: Check if player won**
```python
if "_" not in display:
    game_over = True
    print("\n****************************YOU WIN****************************")
```

**What does this do?**
- `"_" not in display` checks if there are NO underscores left
- If there are no underscores → all letters have been guessed → player wins!

---

### **PART 8: Display the hangman drawing**
```python
print(stages[lives])
```

**What does this do?**
- `stages` is a list with 7 drawings (indices 0 to 6)
- `stages[6]` = empty drawing (6 lives remaining)
- `stages[5]` = head only (5 lives remaining)
- `stages[4]` = head + body (4 lives remaining)
- `stages[0]` = complete hangman (0 lives = GAME OVER)

**Why does it work?**
- As `lives` decreases from 6 to 0, we can use it directly as the index
- When `lives = 3`, it shows `stages[3]` (head + body + left arm)

---

## 🔄 COMPLETE GAME FLOW (One Round)

1. **Show remaining lives**: `3/6 LIVES LEFT`
2. **Ask for a letter**: `Guess a letter: t`
3. **Check if already tried**: If yes → message and return to step 1
4. **Build display**: Go through the word and show what's been guessed
5. **Check if incorrect**: If not in the word → lose a life
6. **Check end conditions**: Won? Lost? → End game
7. **Show hangman drawing** (based on remaining lives)
8. **Return to step 1** (if game hasn't ended)

---

## 📊 VARIABLES REFERENCE TABLE

| Variable | Type | Purpose | Example |
|----------|------|---------|---------|
| `chosen_word` | string | The secret word to guess | `"python"` |
| `lives` | integer | Remaining lives (6 to 0) | `3` |
| `game_over` | boolean | Controls if game has ended | `False` or `True` |
| `correct_letters` | list | Only correct letters guessed | `["p", "y"]` |
| `guessed_letters` | list | All letters attempted | `["p", "y", "z", "a"]` |
| `display` | string | What player sees | `"p_t___"` |
| `guess` | string | Current letter being tried | `"t"` |
| `placeholder` | string | Initial underscores | `"______"` |

---

## 🎨 NICE CUSTOMIZATION IDEAS I WOULD ADD I I KNEW HOW

### **Change difficulty:**
```python
# At the beginning of hangman.py, change:
lives = 10  # Easy mode (more lives)
lives = 6   # Normal mode (classic)
lives = 3   # Hard mode (fewer lives)
```

### **Add words in Spanish:**
In `hangman_words.py`:
```python
word_list = [
    "python",
    "programacion",
    "computadora",
    "elefante",
    "jirafa",
    "mariposa",
    # ... more words
]
```

### **Add hints:**
```python
# In hangman.py, after choosing the word:
if chosen_word == "python":
    print("Hint: It's a programming language 🐍")
```

### **Add difficulty levels:**
```python
print("Choose difficulty:")
print("1. Easy (10 lives)")
print("2. Normal (6 lives)")
print("3. Hard (3 lives)")

difficulty = input("Enter 1, 2, or 3: ")

if difficulty == "1":
    lives = 10
elif difficulty == "2":
    lives = 6
else:
    lives = 3
```

---

## ❓ COMMON ERRORS AND SOLUTIONS

### **Error: `ModuleNotFoundError: No module named 'hangman_words'`**
**Solution:** Make sure all 3 files are in the same folder.

### **Error: `NameError: name 'word_list' is not defined`**
**Solution:** Check that `hangman_words.py` contains `word_list = [...]`

### **Error: `IndexError: list index out of range`**
**Solution:** Make sure `stages` in `hangman_art.py` has 7 drawings (indices 0-6)

### **The game doesn't show the drawings**
**Solution:** Uncomment the line `print(stages[lives])` in `hangman.py`

---

## 🎓 KEY CONCEPTS LEARNED

### **1. Loops (`for` and `while`)**
- `while` repeats as long as a condition is true
- `for` iterates over each element in a sequence

### **2. Lists**
- Store multiple values: `my_list = [1, 2, 3]`
- Add elements: `my_list.append(4)`
- Check if something exists: `if 2 in my_list:`

### **3. Conditionals**
- `if`: executes if condition is true
- `elif`: checks another condition if the first is false
- `else`: executes if all conditions are false

### **4. Imports**
- `import random`: imports an entire module
- `from module import function`: imports a specific function
- Allows code organization in multiple files

### **5. String operators**
- `+` concatenates strings: `"hello" + "world"` → `"helloworld"`
- `*` repeats strings: `"a" * 3` → `"aaa"`
- `in` checks if a substring exists: `"a" in "apple"` → `True`

---

## 👏 CREDITS

This project is based on the classic Hangman game, adapted as a learning exercise for Python beginners.

**Created by:** [Aroa Xinping]  
**Date:** [28/10/2025]  

---

## 📝 NOTES FOR FUTURE REVIEW

If you come back to this code later and don't remember how it works:

1. **Start by reading this README from top to bottom**
2. **Look at the "Code Explanation" section** to understand each part
3. **Check the "Complete Game Flow" section** to understand the game logic
4. **Run the game and add `print()` statements** to see what each variable contains
5. **Experiment!** Change values and see what happens

**Remember:** The best way to learn programming is by doing and making mistakes. Don't be afraid to break the code - you can always fix it! �

---

🎮 **Enjoy your Hangman game!** 🎮
