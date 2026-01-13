class Expense:
    def __init__(self, amount, category, description, date):
        self.amount = float(amount)
        self.category = category
        self.description = description
        self.date = date

    def to_dict(self):
        """Convert object to dictionary for JSON storage"""
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date
        }