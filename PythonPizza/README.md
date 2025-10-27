# 🍕 Python Pizza Deliveries

An interactive pizza ordering system with price calculations.

## What I Learned

### 1. Conditional Logic (if/elif/else)
```python
if size == "S" or size == "s":
    bill = 15
elif size == "M" or size == "m":
    bill = 20
```
Understanding complex conditionals and multiple conditions with `or`.

### 2. Nested If Statements
```python
if pepperoni == "Y":
    if size == "S":
        bill += 2  # Different prices based on size
```
Learned to handle logic within logic for dynamic pricing.

### 3. Variables and Accumulation
```python
bill = 0
bill += 2  # Adding to existing value
```
Building up a total through the program flow.

### 4. ASCII Art
```python
print("""
    // ""--.._
   ||  (_)  _ "-._
""")
```
Using multi-line strings for fun visual elements.

## Features

✨ Case-insensitive input (accepts "S" or "s")  
✨ Dynamic pricing based on size  
✨ Multiple toppings with different prices  
✨ Running total calculation  
✨ Cute ASCII pizza art  
✨ Conversational ordering flow

## Pricing Logic

| Item | Small | Medium | Large |
|------|-------|--------|-------|
| Base Pizza | $15 | $20 | $25 |
| Pepperoni | +$2 | +$3 | +$3 |
| Extra Cheese | +$1 | +$1 | +$1 |

## Challenges Fixed

**Issue:** Users might type lowercase or uppercase  
**Solution:** Check for both with `or` operator (`size == "S" or size == "s"`)

**Issue:** Pepperoni has different prices by size  
**Solution:** Nested if statements to check size again inside pepperoni logic

## Example Order
```
    // ""--.._
   ||  (_)  _ "-._
   ||    _ (_)    '-.
   ||   (_)   __..-'
    \\__..--""

WELCOME TO PYTHON PIZZA DELIVERIES!

- What size pizza do you want? S, M or L: L
okay, size l pizzas are 25$

- Would you like some pepperoni on your pizza? Y or N: y
 With pepperoni, your pizza will be 28 $, 

- Do you also want extra cheese for just 1$ ? Y or N: y
Alright! that will be 29 $ in total, enjoy your meal!
```

## What I'd Improve

- [ ] Use `.lower()` instead of checking both cases
- [ ] Add input validation for invalid options
- [ ] Create a menu with all prices displayed
- [ ] Add more toppings options

---

**Status:** ✅ Completed  
**Date:** October 2024  
**Fun fact:** ASCII art makes it 10x cuter 🍕
