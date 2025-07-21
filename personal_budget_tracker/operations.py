from transaction import Transaction
from data_utils import load_transactions, save_transactions
from budget_utils import calculate_totals, group_by_category

def add_transaction(transaction_data):
    transactions = load_transactions()
    transaction = Transaction(
        transaction_data["description"],
        transaction_data["amount"],
        transaction_data["type"],
        transaction_data["category"]
    )
    transactions.append(transaction.to_dict())
    save_transactions(transactions)
    print("Transaction added successfully!")

def view_transactions():
    transactions = load_transactions()
    if not transactions:
        print("No transactions found.")
        return

    print("\n=== All Transactions ===")
    for t in transactions:
        print(f"\nDate: {t['date']}")
        print(f"Description: {t['description']}")
        print(f"Amount: ${t['amount']:.2f}")
        print(f"Type: {t['type']}")
        print(f"Category: {t['category']}")
        print("-" * 30)

def get_summary():
    transactions = load_transactions()
    if not transactions:
        print("No transactions to summarize.")
        return

    total_income, total_expenses = calculate_totals(transactions)
    categories = group_by_category(transactions)

    print("\n=== Budget Summary ===")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Net Balance: ${(total_income - total_expenses):.2f}")

    print("\n=== Category Breakdown ===")
    for category, amount in categories.items():
        print(f"{category}: ${amount:.2f}")
