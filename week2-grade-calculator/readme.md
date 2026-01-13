# Student Grade Calculator 
## Project Description 
A comprehensive grade calculator that processes multiple students' marks, calculates grades with personalized comments, and provides class statistics. 

## What I Learned 
1. **Conditional Logic**: Using if/elif/else for decision making
2. **Lists**: Storing and manipulating collections of data
3. **Loops**: Using for and while loops for repetition
4. **Error Handling**: Using try-except to handle invalid inputs
5. **Functions**: Organizing code into reusable blocks


## Features 
- ✅ Processes multiple students
- ✅ Calculates grades based on custom grading system
- ✅ Provides personalized comments for each student
- ✅ Calculates class statistics (average, highest, lowest)
- ✅ Formatted table output with color coding
- ✅ Input validation for all user inputs
- ✅ Error handling for edge cases
- ✅ Search functionality for specific students
- ✅ Save results to file option


## How to Run 
```bash 
# Navigate to project folder 
cd week2-grade-calculator
# Run the program 
python grade_calculator.py
# Sample test with provided data 
python grade_calculator.py < test_students.txt
```

## Grading System 
- A: 90-100 (Excellent!)
- B: 80-89 (Very Good!)
- C: 70-79 (Good)
- D: 60-69 (Needs Improvement)
- F: 0-59 (Failed - Please seek help)

## Sample Output 
``` 
===========================================
STUDENT GRADE CALCULATOR
===========================================
Number of students:3
=== STUDENT 1 ===
Name: John Smith
Math: 85
Science: 92
English: 88

=== STUDENT 2 ===
Name: Sarah Johnson
Math: 78
Science: 81
English: 85

===========================================
RESULTS SUMMARY
===========================================
Name | Avg | Grade | Comment
---------------+-----+-------+-----------------
John Smith | 88.3| B | Very Good!
Sarah Johnson | 81.3| B |Very Good!


===========================================
CLASS STATISTICS
===========================================
Total Students: 2
Class Average: 84.8
Highest Average: 88.3 (John Smith)
Lowest Average: 81.3 (Sarah Johnson)
```
## Challenges & Solutions 
**Challenge**: Handling invalid marks input 

**Solution**: Used while loop with try-except to validate 

**Challenge**: Formatting the results table 

**Solution**: Used string formatting with fixed widths 

**Challenge**: Calculating multiple statistics 

**Solution**: Used list comprehensions and built-in functions
