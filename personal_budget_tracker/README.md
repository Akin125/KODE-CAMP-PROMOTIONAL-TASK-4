# 💰 Personal Budget Tracker

A terminal-based Python application for tracking personal income and expenses with category-based organization and summary reports.

## 🌟 Key Features

- Track income and expenses with descriptions and categories
- View detailed transaction history
- Get summary reports with totals and category breakdowns
- Data persistence using JSON storage
- Clean, modular code structure

## 📁 Project Structure

```
personal_budget_tracker/
├── main.py             # Entry point and menu
├── transaction.py      # Transaction class definition
├── operations.py       # Add/view/summary functions
├── budget_utils.py     # Grouping and calculations
├── data_utils.py       # JSON load/save logic
├── transactions.json   # Auto-created data storage
└── README.md          # Documentation
```

## 💻 How to Use

1. Run the application:
   ```bash
   python main.py
   ```

2. Choose from the menu options:
   - Add Transaction (1)
   - View Transactions (2)
   - View Summary (3)
   - Exit (4)

### Adding Transactions
- Enter transaction description
- Specify the amount
- Choose type (income/expense)
- Select a category

### Viewing Summary
Shows:
- Total income
- Total expenses
- Net balance
- Category-wise breakdown

## 📦 Requirements

- Python 3.6 or higher
- No external dependencies

## 💾 Data Storage

Transactions are stored in `transactions.json` in the following format:
```json
[
    {
        "description": "Salary",
        "amount": 5000.00,
        "type": "income",
        "category": "Work",
        "date": "2025-07-21 14:30:00"
    }
]
```

