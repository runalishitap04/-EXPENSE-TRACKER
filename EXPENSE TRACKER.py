def show_menu():
    print("\n=== Expense Tracker Menu ===")
    print("1. Add Expense")
    print("2. Show Summary")
    print("3. Exit")

def add_expense(expenses):
    category = input("Enter category (e.g., Food, Travel, Bills): ").strip()
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount < 0:
                print("Amount can't be negative. Try again.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")
    # Append expense as tuple (category, amount)
    expenses.append((category, amount))
    print(f"Added expense: {category} - {amount}")

def show_summary(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    summary = {}
    total = 0.0
    
    for cat, amt in expenses:
        summary[cat] = summary.get(cat, 0) + amt
        total += amt
    
    print("\n--- Expense Summary ---")
    for cat, amt in summary.items():
        print(f"{cat}: ₹{amt:.2f}")
    print(f"Total Expenses: ₹{total:.2f}")

def main():
    expenses = []
    while True:
        show_menu()
        choice = input("Choose an option (1-3): ").strip()
        
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            show_summary(expenses)
        elif choice == '3':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
