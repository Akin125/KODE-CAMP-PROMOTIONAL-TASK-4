def calculate_totals(transactions):
    total_income = sum(t['amount'] for t in transactions if t['type'] == 'income')
    total_expenses = sum(t['amount'] for t in transactions if t['type'] == 'expense')
    return total_income, total_expenses

def group_by_category(transactions):
    categories = {}
    for t in transactions:
        category = t['category']
        amount = t['amount']
        if category in categories:
            if t['type'] == 'expense':
                categories[category] -= amount
            else:
                categories[category] += amount
        else:
            categories[category] = amount if t['type'] == 'income' else -amount
    return categories
