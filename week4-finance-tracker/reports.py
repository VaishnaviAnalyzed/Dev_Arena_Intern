def generate_summary(expenses):
    """Calculates total spent and breakdown by category"""
    if not expenses:
        return "No expenses recorded."

    total = sum(item['amount'] for item in expenses)
    categories = {}
    
    for item in expenses:
        cat = item['category']
        categories[cat] = categories.get(cat, 0) + item['amount']

    report = f"\n--- Financial Report ---\nTotal Spent: ${total:.2f}\n"
    report += "Breakdown by Category:\n"
    for cat, amt in categories.items():
        report += f" - {cat}: ${amt:.2f}\n"
    
    return report