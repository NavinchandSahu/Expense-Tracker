## Expense Tracker App 💰📊

A desktop-based Expense Tracker built using Python, PyQt6, and SQLite.  
This application helps users record, view, and delete daily spending while categorizing expenses for better financial control.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech-Stack](#tech-stack)
- [How-It-Works](#how-it-works)
- [Installation](#installation)

---

## Overview
Keeping track of expenses is essential, and this Expense Tracker makes it simple with a clean GUI interface.  
Users can enter the Date, Category, Amount, and Description, and the data is immediately stored inside a SQLite database.  
The app displays all entries in a table and allows deleting selected records—all without touching the database manually.

---

## Features
- Modern PyQt6 interface
- Add & remove expense records
- Multiple spending categories
- Automatic storage in SQLite database
- Dynamic table that reloads instantly
- Easy-to-use input fields
- Perfect for budgeting and personal finance tracking

---

## Tech Stack
- **Language:** Python  
- **GUI Framework:** PyQt6  
- **Database:** SQLite  
- **Libraries Used:** `PyQt6`, `sqlite3`, `QSqlDatabase`

---

## How It Works
1. User enters expense details  
2. App writes data to the SQLite database  
3. Table refreshes to show the latest entries  
4. User can select a row & delete it anytime

---

## Installation
```bash
git clone https://github.com/NavinchandSahu/Expense-Tracker.git
cd Expense-Tracker
pip install pyqt6
python expensetracker_main.py
````

---
