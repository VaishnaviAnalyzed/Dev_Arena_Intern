# finance_tracker/main.py - Simplified version

class FinanceTracker:
    def __init__(self):
        self.expenses = []
    
    def run(self):
        print("=" * 60)
        print("          PERSONAL FINANCE TRACKER")
        print("=" * 60)
        
        while True:
            print("\n" + "=" * 40)
            print("              MAIN MENU")
            print("=" * 40)
            print("1. Add New Expense")
            print("2. View All Expenses")
            print("3. Search Expenses")
            print("4. Generate Monthly Report")
            print("5. View Category Breakdown")
            print("6. Set/Update Budget")
            print("7. Export Data to CSV")
            print("8. View Statistics")
            print("9. Backup/Restore Data")
            print("0. Exit")
            print("=" * 40)
            
            choice = input("\nEnter your choice (0-9): ").strip()
            
            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.view_expenses()
            elif choice == '3':
                self.search_expenses()
            elif choice == '4':
                self.generate_monthly_report()
            elif choice == '5':
                self.view_category_breakdown()
            elif choice == '6':
                self.set_budget()
            elif choice == '7':
                self.export_data()
            elif choice == '8':
                self.view_statistics()
            elif choice == '9':
                self.backup_restore()
            elif choice == '0':
                print("\n" + "=" * 60)
                print("Thank you for using Personal Finance Tracker!")
                print("=" * 60)
                break
            else:
                print("Invalid choice! Please enter 0-9.")
    
    def add_expense(self):
        print("\n--- ADD NEW EXPENSE ---")
        # Implementation would go here
        print("Expense added successfully!")
    
    def view_expenses(self):
        print("\n--- ALL EXPENSES ---")
        # Implementation would go here
        print("Displaying all expenses...")
    
    def search_expenses(self):
        print("\n--- SEARCH EXPENSES ---")
        # Implementation would go here
        print("Searching expenses...")
    
    def generate_monthly_report(self):
        print("\n--- MONTHLY REPORT ---")
        # Implementation would go here
        print("Generating monthly report...")
    
    def view_category_breakdown(self):
        print("\n--- CATEGORY BREAKDOWN ---")
        # Implementation would go here
        print("Showing category breakdown...")
    
    def set_budget(self):
        print("\n--- SET/UPDATE BUDGET ---")
        # Implementation would go here
        print("Setting budget...")
    
    def export_data(self):
        print("\n--- EXPORT DATA ---")
        # Implementation would go here
        print("Exporting data...")
    
    def view_statistics(self):
        print("\n--- STATISTICS ---")
        # Implementation would go here
        print("Showing statistics...")
    
    def backup_restore(self):
        print("\n--- BACKUP/RESTORE ---")
        # Implementation would go here
        print("Managing backups...")

def main():
    tracker = FinanceTracker()
    tracker.run()

if __name__ == "__main__":
    main()