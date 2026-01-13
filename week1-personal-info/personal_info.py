# Personal Information Manager
# My first Python project by Vaishnavi Chandore

# Welcome message
print("=" * 40)
print("    PERSONAL INFORMATION MANAGER")
print("=" * 40)
print()

# Store static information
name = "Vaishnavi Chandore"
age = 25
city = "Pune"
hobby = "Playing Guitar & Listening Music"

# Get user input
print("Please tell me about yourself:")
print("-" * 30)

favorite_food = input("What's your favorite food? ")
while favorite_food == "":
    print("Please enter a valid food!")
    favorite_food = input("What's your favorite food? ")

favorite_color = input("What's your favorite color? ")
while favorite_color == "":
    print("Please enter a valid color!")
    favorite_color = input("What's your favorite color? ")

# Calculate age in months
age_in_months = age * 12

# Display all information
print()
print("=" * 40)
print("        YOUR INFORMATION")
print("=" * 40)
print()

print(f"Name: {name}")
print(f"Age: {age} years ({age_in_months} months old)")
print(f"City: {city}")
print(f"Hobby: {hobby}")
print()
print(f"Favorite Food: {favorite_food}")
print(f"Favorite Color: {favorite_color}")
print()

# Goodbye message
print("=" * 40)
print("Thanks for using this program!")
print("=" * 40)