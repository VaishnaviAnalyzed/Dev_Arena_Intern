# Contact Management System 
## Project Description 
A comprehensive contact management system built with Python using dictionaries and functions. This system allows users to manage their contacts with full CRUD operations, search functionality, and data persistence. 

## What I Learned 
1. **Functions**: Creating reusable, organized code blocks
2. **Dictionaries**: Storing and retrieving data using key-value pairs
3. **String Methods**: Advanced text manipulation and formatting
4. **File Operations**: Saving and loading data from JSON files
5. **Input Validation**: Ensuring data quality and preventing errors
6. **Error Handling**: Gracefully handling unexpected situations


## Features 
- ✅ Add new contacts with validation
- ✅ Search contacts by name (partial matching supported)
- ✅ Update existing contact information
- ✅ Delete contacts with confirmation
- ✅ View all contacts in formatted display
- ✅ Save contacts to JSON file automatically
- ✅ Load contacts from file on startup
- ✅ Export contacts to CSV format
- ✅ Contact statistics and analytics
- ✅ Phone number and email validation
- ✅ User-friendly menu interface
- ✅ Error handling for all operations


## How to Run 
```
bash
# Navigate to project folder
cd week3-contact-manager

# Install any requirements
pip install -r requirements.txt

# (if needed)

# Run the program
python contacts_manager.py

# Run tests
python test_contacts.py
```

## Data Structure 
```
python contacts =
{
"John Doe":
{
"phone": "+1234567890",
"email": "john@example.com",
"address": "123 Main St",
"group": "Friends"
},

"Jane Smith":
{
"phone": "+0987654321",
"email": "jane@example.com",
"address": "456 Oak Ave",
"group": "Work"
}
}
```

## Sample Menu 
``` 
===========================================
CONTACT MANAGEMENT SYSTEM
===========================================
1. Add New Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. View All Contacts
6. Export to CSV
7. View Statistics
8. Exit

Enter your choice (1-8):
```

## Sample Output 
``` 
Search Results for 'john':
 ------------------------------------------
1. John Doe
Phone: +1234567890
Email: john@example.com
Address: 123 Main St
Group: Friends

2. Johnny Appleseed
Phone: +5551234567
Email: johnny@apple.com
Address: 789 Orchard Rd
Group: Family
------------------------------------------

Found 2 contacts matching 'john'

Statistics:
- Total Contacts: 15
- Friends: 5 contacts
- Work: 7 contacts
- Family: 3 contacts
```

## Challenges & Solutions 
**Challenge**: Handling duplicate contact names 

**Solution**: Added option to view all matches and select which to update 

**Challenge**: Phone number validation across different formats 

**Solution**: Created flexible validation function supporting multiple formats 

**Challenge**: Efficient search with partial matching 

**Solution**: Used dictionary comprehension with lower() for case-insensitive search 

**Challenge**: Data persistence with JSON 

**Solution**: Used json module with proper error handling for file operations
