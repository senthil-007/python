import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


def initialize_file():
    """Create the CSV file if it does not exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])


def add_expense():
    """Add a new expense."""
    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()

    while True:
        try:
            amount = float(input("Enter amount: ₹"))
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid amount.")

    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print("Expense added successfully!")


def view_expenses():
    """Display all recorded expenses."""
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        expenses = list(reader)

    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n" + "-" * 70)
    print(f"{'Date':<15}{'Category':<15}{'Description':<25}{'Amount':>10}")
    print("-" * 70)

    for expense in expenses:
        print(
            f"{expense['Date']:<15}"
            f"{expense['Category']:<15}"
            f"{expense['Description']:<25}"
            f"₹{float(expense['Amount']):>9.2f}"
        )

    print("-" * 70)


def calculate_total():
    """Calculate total expenses."""
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for expense in reader:
            total += float(expense["Amount"])

    print(f"\nTotal Expenses: ₹{total:.2f}")


def category_summary():
    """Display expenses grouped by category."""
    summary = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for expense in reader:
            category = expense["Category"]
            amount = float(expense["Amount"])

            summary[category] = summary.get(category, 0) + amount

    if not summary:
        print("\nNo expenses found.")
        return

    print("\nCategory-wise Expense Summary")
    print("-" * 40)

    for category, amount in summary.items():
        print(f"{category:<20} ₹{amount:.2f}")


def monthly_summary():
    """Display expenses for the current month."""
    current_month = datetime.now().strftime("%Y-%m")
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for expense in reader:
            if expense["Date"].startswith(current_month):
                total += float(expense["Amount"])

    print(f"\nExpenses for {current_month}: ₹{total:.2f}")


def main():
    """Main application menu."""
    initialize_file()

    while True:
        print("\n========== EXPENSE TRACKER ==========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Category Summary")
        print("5. Monthly Summary")
        print("6. Exit")
        print("=====================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            calculate_total()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            monthly_summary()

        elif choice == "6":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
