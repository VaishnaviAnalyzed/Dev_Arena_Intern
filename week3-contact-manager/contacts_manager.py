# Contact Management System
# Week 3 Project - Functions & Dictionaries

import json
import re
from datetime import datetime
import os

# --- VALIDATION FUNCTIONS ---

def validate_phone(phone):
    """Validate phone number format (10-15 digits)"""
    digits = re.sub(r'\D', '', phone)
    if 10 <= len(digits) <= 15:
        return True, digits
    return False, None

def validate_email(email):
    """Validate email format using Regex"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# --- CORE FUNCTIONS ---

def add_contact(contacts):
    """Add a new contact or redirect to update if exists"""
    print("\n--- ADD NEW CONTACT ---")
    while True:
        name = input("Enter contact name: ").strip()
        if name:
            if name in contacts:
                print(f"Contact '{name}' already exists!")
                choice = input("Do you want to update instead? (y/n): ").lower()
                if choice == 'y':
                    return update_contact(contacts, name)
                return contacts
            break
        print("Name cannot be empty!")
    
    while True:
        phone = input("Enter phone number: ").strip()
        is_valid, cleaned_phone = validate_phone(phone)
        if is_valid: break
        print("Invalid phone! Enter 10-15 digits.")
    
    while True:
        email = input("Enter email (optional, press Enter to skip): ").strip()
        if not email or validate_email(email): break
        print("Invalid email format!")
    
    address = input("Enter address (optional): ").strip()
    group = input("Group (Friends/Work/Family/Other): ").strip() or "Other"
    
    contacts[name] = {
        'phone': cleaned_phone,
        'email': email if email else None,
        'address': address if address else None,
        'group': group,
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat()
    }
    print(f"✅ Contact '{name}' added!")
    return contacts

def update_contact(contacts, name):
    """Update existing contact info"""
    print(f"\n--- UPDATING: {name} ---")
    contact = contacts[name]
    
    print("Press Enter to keep current value.")
    
    # Update Phone
    new_phone = input(f"Phone [{contact['phone']}]: ").strip()
    if new_phone:
        valid, clean = validate_phone(new_phone)
        if valid: contact['phone'] = clean
    
    # Update Email
    new_email = input(f"Email [{contact['email']}]: ").strip()
    if new_email and validate_email(new_email):
        contact['email'] = new_email
        
    contact['updated_at'] = datetime.now().isoformat()
    print("✅ Contact updated!")
    return contacts

def search_contacts(contacts, search_term):
    """Partial match search"""
    search_term = search_term.lower()
    return {n: i for n, i in contacts.items() if search_term in n.lower()}

def display_results(results):
    if not results:
        print("No contacts found.")
        return
    for name, info in results.items():
        print(f"\n👤 {name}")
        print(f"   📞 {info['phone']} | 👥 {info['group']}")
        if info['email']: print(f"   📧 {info['email']}")

# --- FILE PERSISTENCE ---

def save_contacts(contacts):
    with open('contacts_data.json', 'w') as f:
        json.dump(contacts, f, indent=4)

def load_contacts():
    if os.path.exists('contacts_data.json'):
        with open('contacts_data.json', 'r') as f:
            return json.load(f)
    return {}

# --- MAIN MENU ---

def main():
    contacts = load_contacts()
    while True:
        print("\n" + "="*30)
        print(" CONTACT MANAGEMENT SYSTEM")
        print("="*30)
        print("1. Add/Update Contact")
        print("2. Search Contacts")
        print("3. View All")
        print("4. Save & Exit")
        
        choice = input("\nSelect (1-4): ")
        
        if choice == '1':
            contacts = add_contact(contacts)
        elif choice == '2':
            term = input("Search name: ")
            display_results(search_contacts(contacts, term))
        elif choice == '3':
            display_results(contacts)
        elif choice == '4':
            save_contacts(contacts)
            print("Data saved. Goodbye!")
            break

if __name__ == "__main__":
    main()