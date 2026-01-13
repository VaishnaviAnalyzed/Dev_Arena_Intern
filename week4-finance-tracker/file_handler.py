import json
import os

DATA_FILE = "data/expenses.json"

def save_expenses(expenses_list):
    """Saves a list of expense dictionaries to JSON"""
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(expenses_list, f, indent=4)

def load_expenses():
    """Loads expenses from JSON; returns empty list if file doesn't exist"""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []