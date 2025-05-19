# MPIN Strength Checker 🔒

This Python project provides a utility to evaluate the strength of a Mobile PIN (MPIN) based on:
- Commonly used MPINs
- Personal demographic patterns like date of birth, spouse's DOB, and wedding anniversary

## 🚀 Features

- Detects weak MPINs based on known patterns
- Evaluates 4-digit and 6-digit MPINs
- Flags use of dates or common numbers
- Comes with a suite of test cases

## 🧠 Logic Highlights

1. **Common MPINs Check**: Matches against a known list (`1234`, `0000`, etc.)
2. **Demographic Match Check**: Checks if MPIN matches parts of DOB, spouse’s DOB, or anniversary
3. **Strength Evaluation**: Flags as `WEAK` or `STRONG` with reasons

## 🛠️ Usage

Run the main program:
```bash
python mpin_checker.py  
