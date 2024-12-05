import csv
from datetime import datetime

# Initialize the expenses list
expenses = []

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    description = input("Enter description: ")
    category = input("Enter category (e.g., food, transport): ")
    amount = float(input("Enter amount: "))
    expenses.append({"date": date, "description": description, "category": category, "amount": amount})
    print("Expense added successfully!")

def view_expenses():
    print("\n--- Your Expenses ---")
    for expense in expenses:
        print(f"{expense['date']} | {expense['description']} | {expense['category']} | ${expense['amount']:.2f}")

def category_summary():
    summary = {}
    for expense in expenses:
        category = expense["category"]
        summary[category] = summary.get(category, 0) + expense["amount"]
    print("\n--- Category-wise Summary ---")
    for category, total in summary.items():
        print(f"{category}: ${total:.2f}")

def monthly_summary():
    month = input("Enter month (YYYY-MM): ")
    total = sum(expense["amount"] for expense in expenses if expense["date"].startswith(month))
    print(f"\nTotal spending for {month}: ${total:.2f}")

def save_to_file():
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "description", "category", "amount"])
        writer.writeheader()
        writer.writerows(expenses)
    print("Expenses saved to file!")

def load_from_file():
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["amount"] = float(row["amount"])
                expenses.append(row)
        print("Expenses loaded successfully!")
    except FileNotFoundError:
        print("No saved data found.")

def main():
    load_from_file()
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Category Summary")
        print("4. Monthly Summary")
        print("5. Save & Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category_summary()
        elif choice == "4":
            monthly_summary()
        elif choice == "5":
            save_to_file()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
