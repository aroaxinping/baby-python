# 🐱 Rescue The Cat

A text-based adventure game where your choices determine if you save the cat or meet your doom.

## What I Learned

### 1. Raw Strings for ASCII Art
```python
print(r'''
      |\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
''')
```
The `r` prefix makes a "raw string" - it preserves backslashes and special characters without escaping them. Perfect for ASCII art!

### 2. Nested Conditionals Create Story Branches
```python
if q1 == "left":              # First decision
    if q2 == "wait":          # Second decision (only if left)
        if finalq == "yellow": # Third decision (only if wait)
            print("You win!")
```
Each level of indentation = a deeper choice in the story. Wrong choice = skip everything nested inside.

### 3. Multiple Losing Conditions
```python
if finalq == "blue" or finalq == "red":
    print("GAME OVER")
```
Using `or` to handle multiple fail states efficiently.

### 4. Game Design Philosophy
- **Only 1 winning path** out of 8 possible combinations
- **Immediate consequences** - wrong choice = instant game over
- **Progressive difficulty** - must survive 3 decisions

## The Winning Path
```
🚶 Start at crossroad
  ↓
← Go LEFT (right = lost forever)
  ↓
⏳ WAIT for boat (swim = drowned)
  ↓
🚪 Choose YELLOW door (red/blue = death)
  ↓
🎉 SUCCESS! Cat rescued!
```

**Probability of winning by random choices:** 12.5% (1/8)

## Game Map
```
                    START
                      |
            ┌─────────┴─────────┐
          LEFT                RIGHT
            |                   |
         LAKE              ☠️ LOST
            |
      ┌─────┴─────┐
    WAIT         SWIM
      |            |
   ISLAND      ☠️ DROWNED
      |
   3 DOORS
      |
  ┌───┼───┐
RED  YELLOW  BLUE
 |      |      |
☠️    🎉     ☠️
```

## Code Structure Breakdown
```python
# Level 1: Crossroad (2 choices)
if left:
    # Level 2: Lake (2 choices, nested in left)
    if wait:
        # Level 3: Doors (3 choices, nested in wait)
        if yellow:
            WIN
        else:
            LOSE
    else swim:
        LOSE
else right:
    LOSE
```

## Important Discovery

**The `else` placement matters!**
```python
if q1 == "right":
    print("GAME OVER")
else:  # This else applies ONLY to the if above it
    print("invalid choice")
```

This `else` doesn't catch all invalid inputs - it only applies to the immediate `if`. Learned that `else` is always paired with its closest `if`.

## Example Playthrough

**💀 Losing path:**
```
You're on a cross road. Where do you want to go? right
GAME OVER, YOU GOT LOST.
```

**🎉 Winning path:**
```
You're on a cross road. Where do you want to go? left
You've come to a lake. Type wait or swim: wait
You have arrived at the island unharmed.
Which colour door? yellow
Congratulations! You saved the cat!
```

## Challenges & Solutions

| Challenge | Solution | What I Learned |
|-----------|----------|----------------|
| ASCII art broke with `\` characters | Used `r'''` raw string | Special characters need special handling |
| Confusing nested logic | Drew it out as a tree diagram | Visualizing helps understand flow |
| `else` triggered at wrong times | Understood `else` pairs with closest `if` | Scope and structure matter |

## What I'd Improve Next Time

**Priority improvements:**
- [ ] Add `.lower()` to accept any capitalization
- [ ] Better input validation (handle typos)
- [ ] Fix typo: "Wich" → "Which"

**Nice-to-have features:**
- [ ] Add restart option
- [ ] More atmospheric descriptions
- [ ] Easter eggs in losing paths
- [ ] Multiple winning paths with different endings

## Key Takeaway

> "Nested if statements are like Russian nesting dolls - you only see what's inside if you open the outer layers first. Each wrong choice closes all the doors inside."

---

**Status:** ✅ Completed  
**Date:** October 2024  
**Difficulty:** ⭐⭐ (Intermediate)  
**Lines of code:** ~20  
**Possible outcomes:** 5 (1 win, 4 game overs)  
**Fun fact:** The cat was yellow all along 🐱💛
