import json
import os

TRANSACTIONS_FILE = "transactions.json"

def load_transactions():
    if not os.path.exists(TRANSACTIONS_FILE):
        return []
    try:
        with open(TRANSACTIONS_FILE, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_transactions(transactions):
    with open(TRANSACTIONS_FILE, 'w') as file:
        json.dump(transactions, file, indent=4)
