# 💰 Tip Calculator

Splits tips between people.

## What I Learned
- Clean user input (remove "%" symbol)
- Convert strings to numbers (`float()`, `int()`)
- Round decimals properly
- Use `.is_integer()` to format output

## Smart Features I added
✨ Handles "15%" or "15" input  
✨ Removes ugly .0 from whole numbers (shows "5" not "5.0")  
✨ Cute welcome message!

## Challenges Fixed
- **Issue:** Crashed with "%" symbol → Fixed by removing it before converting
- **Issue:** Showed 5.0 instead of 5 → Fixed with `.is_integer()` check

---
✅ Done | October 2025
