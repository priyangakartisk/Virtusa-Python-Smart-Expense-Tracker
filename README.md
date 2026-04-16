# Virtusa-Python-Smart-Expense-Tracker
The Smart Expense Tracker is a simple Python console application that helps users record, manage, and analyze their daily expenses.
It allows users to:

Add daily expenses

View all recorded expenses

Generate spending summaries

Identify highest spending categories

# Concepts Used

File Handling (CSV)

Functions and Modular Programming

Dictionaries (defaultdict)

Loops and Conditional Statements

Exception Handling

# MY OUTPUT
```
PS D:\python project> python expense_tracker.py

===== Smart Expense Tracker =====
1. Add Expense
2. View Expenses
3. Show Summary
4. Exit
Enter choice: 1

Enter date (YYYY-MM-DD) or press Enter for today: 
Enter category (Food, Travel, Bills, etc.): Food
Enter amount: 120
Enter description: Lunch
✅ Expense added successfully!


===== Smart Expense Tracker =====
1. Add Expense
2. View Expenses
3. Show Summary
4. Exit
Enter choice: 1

Enter date (YYYY-MM-DD) or press Enter for today: 
Enter category (Food, Travel, Bills, etc.): Travel
Enter amount: 300
Enter description: Bus ticket
✅ Expense added successfully!


===== Smart Expense Tracker =====
1. Add Expense
2. View Expenses
3. Show Summary
4. Exit
Enter choice: 2

--- All Expenses ---
Date: 2026-04-16 | Category: Food | Amount: $120 | Desc: Lunch
Date: 2026-04-16 | Category: Travel | Amount: $300 | Desc: Bus ticket


===== Smart Expense Tracker =====
1. Add Expense
2. View Expenses
3. Show Summary
4. Exit
Enter choice: 3

--- Expense Summary ---
Food: $120.00
Travel: $300.00

Total Spending: $420.00
Highest Spending Category: Travel


===== Smart Expense Tracker =====
1. Add Expense
2. View Expenses
3. Show Summary
4. Exit
Enter choice: 4

Goodbye!
```
