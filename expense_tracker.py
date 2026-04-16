import csv
from datetime import datetime
from collections import defaultdict

FILE_NAME = "expenses.csv"


def add_expense():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if date == "":
        date = datetime.now().strftime("%Y-%m-%d")

    category = input("Enter category (Food, Travel, Bills, etc.): ").strip().title()

    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be positive.\n")
            return
    except ValueError:
        print("Invalid amount.\n")
        return

    description = input("Enter description: ").strip()

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("✅ Expense added successfully!\n")


def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            print("\n--- All Expenses ---")
            for row in reader:
                print(f"Date: {row[0]} | Category: {row[1]} | Amount: ${row[2]} | Desc: {row[3]}")
            print()
    except FileNotFoundError:
        print("No expenses found.\n")


def show_summary():
    category_total = defaultdict(float)
    total = 0

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                category = row[1]
                amount = float(row[2])
                category_total[category] += amount
                total += amount

        print("\n--- Expense Summary ---")
        for cat, amt in category_total.items():
            print(f"{cat}: ${amt:.2f}")

        print(f"\nTotal Spending: ${total:.2f}")

        # Highest category
        if category_total:
            highest = max(category_total, key=category_total.get)
            print(f"Highest Spending Category: {highest}")
        print()

    except FileNotFoundError:
        print("No data available.\n")


def main():
    while True:
        print("===== Smart Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Summary")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()