from operations import add_transaction, view_transactions, get_summary
from data_utils import load_transactions, save_transactions

def display_menu():
    print("\n=== Personal Budget Tracker ===")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. View Summary")
    print("4. Exit")
    return input("Choose an option (1-4): ")

def main():
    while True:
        choice = display_menu()

        if choice == "1":
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            type_ = input("Enter type (income/expense): ").lower()
            category = input("Enter category: ")

            transaction = {
                "description": description,
                "amount": amount,
                "type": type_,
                "category": category
            }
            add_transaction(transaction)

        elif choice == "2":
            view_transactions()

        elif choice == "3":
            get_summary()

        elif choice == "4":
            print("Thank you for using Personal Budget Tracker!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
