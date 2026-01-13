# Student Grade Calculator
# Week 2 Project - Control Flow & Data Structures

def calculate_grade(average):
    """Calculate grade based on average marks"""
    if average >= 90:
        return 'A', 'Excellent! Keep up the great work!'
    elif average >= 80:
        return 'B', 'Very Good! You\'re doing well.'
    elif average >= 70:
        return 'C', 'Good. Room for improvement.'
    elif average >= 60:
        return 'D', 'Needs Improvement. Please study more.'
    else:
        return 'F', 'Failed. Please seek help from teacher.'

def get_valid_number(prompt, min_val=0, max_val=100):
    """Get a valid number within specified range"""
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a number between {min_val} and {max_val}")
        except ValueError:
            print("Invalid input! Please enter a number.")

def main():
    print("=" * 50)
    print("      STUDENT GRADE CALCULATOR")
    print("=" * 50)
    print()
    
    # Get number of students with validation
    while True:
        try:
            num_students = int(input("Enter number of students: "))
            if num_students > 0:
                break
            else:
                print("Please enter a positive number!")
        except ValueError:
            print("Invalid input! Please enter a whole number.")
    
    # Initialize lists to store data
    student_names = []
    student_marks = []  # Will be list of lists
    student_results = []  # Will store (average, grade, comment)
    
    # Collect data for each student
    for i in range(num_students):
        print(f"\n=== STUDENT {i+1} ===")
        
        # Get student name
        name = input("Student name: ")
        while name.strip() == "":
            print("Name cannot be empty!")
            name = input("Student name: ")
        student_names.append(name)
        
        # Get marks for 3 subjects
        print("Enter marks (0-100):")
        math = get_valid_number("Math: ")
        science = get_valid_number("Science: ")
        english = get_valid_number("English: ")
        
        # Store marks
        student_marks.append([math, science, english])
        
        # Calculate average
        average = (math + science + english) / 3
        
        # Get grade and comment
        grade, comment = calculate_grade(average)
        
        # Store results
        student_results.append({
            'average': average,
            'grade': grade,
            'comment': comment
        })
    
    # Display results
    print("\n" + "=" * 50)
    print("            RESULTS SUMMARY")
    print("=" * 50)
    print(f"{'Name':<20} | {'Avg':>5} | {'Grade':^5} | Comment")
    print("-" * 60)
    
    for i in range(num_students):
        name = student_names[i]
        avg = student_results[i]['average']
        grade = student_results[i]['grade']
        comment = student_results[i]['comment']
        
        print(f"{name:<20} | {avg:>5.1f} | {grade:^5} | {comment}")
    
    # Calculate and display statistics
    if num_students > 0:
        averages = [result['average'] for result in student_results]
        class_avg = sum(averages) / len(averages)
        max_avg = max(averages)
        min_avg = min(averages)
        max_index = averages.index(max_avg)
        min_index = averages.index(min_avg)
        
        print("\n" + "=" * 50)
        print("          CLASS STATISTICS")
        print("=" * 50)
        print(f"Total Students: {num_students}")
        print(f"Class Average: {class_avg:.1f}")
        print(f"Highest Average: {max_avg:.1f} ({student_names[max_index]})")
        print(f"Lowest Average: {min_avg:.1f} ({student_names[min_index]})")
    
    print("\n" + "=" * 50)
    print("Thank you for using the Grade Calculator!")
    print("=" * 50)

if __name__ == "__main__":
    main()