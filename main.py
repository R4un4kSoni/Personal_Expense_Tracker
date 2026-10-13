
import json

try:
    with open("data.json", "r") as data:
        total_expense = json.load(data)

except FileNotFoundError:
    total_expense = {}

except json.JSONDecodeError:
    total_expense = {}


def save_expenses():
    """Save the dictionary into data.json."""
    with open("data.json", "w") as data:
        json.dump(total_expense, data, indent=4)


def add_expense(name, amount):
    if not name:
        print("Expense name cannot be empty.")
        return

    if amount < 0:
        print("Expense amount cannot be negative.")
        return

    if name in total_expense:
        total_expense[name] += amount
    else:
        total_expense[name] = amount

    save_expenses()

    print(f"Expense '{name}' added successfully!")


def see_total():
    total = sum(total_expense.values())

    print("\n--- Expense Summary ---")

    if not total_expense:
        print("No expenses recorded yet.")
        print("Total amount spent: $0.00")
        return

    for expense, amount in total_expense.items():
        print(f"{expense}: ${amount:.2f}")

    print(f"Total amount spent: ${total:.2f}")


def see_all_expenses():
    print("\n--- All Expenses ---")

    if not total_expense:
        print("No expenses recorded yet.")
        return

    for expense, amount in total_expense.items():
        print(f"{expense}: ${amount:.2f}")


while True:
    name_of_expense = input(
        "\nEnter expense name (or 'see total', "
        "'see all expenses', 'exit'): "
    ).strip()

    if name_of_expense.lower() == "exit":
        print("Thank you for using the Expense Tracker!")
        break

    elif name_of_expense.lower() == "see total":
        see_total()
        continue

    elif name_of_expense.lower() == "see all expenses":
        see_all_expenses()
        continue

    elif not name_of_expense:
        print("Please enter an expense name.")
        continue

    amount_of_expense = input(
        "Enter expense amount (or 'skip' to cancel): "
    ).strip()

    if amount_of_expense.lower() == "skip":
        print("Expense skipped.")
        continue

    try:
        amount_of_expense = float(amount_of_expense)
        add_expense(name_of_expense, amount_of_expense)

    except ValueError:
        print("Invalid amount. Please enter a number.")