# Program Name: Lab12.py
# Course: IT1114/Section XXX
# Student Name: Daniel Urdaneta
# Assignment Number: Lab12
# Due Date: 12/3/2024
# Purpose: This program reads grades from a file, calculates average scores for each section, 
#          and outputs the results.
# Resources: Python documentation, class notes.

# Grade conversion table
grade_to_score = {
    'A': 100,
    'B': 89,
    'C': 79,
    'D': 74,
    'F': 69
}

def main():
    # Dictionary to store section grades
    section_grades = {}

    # Open the grades.txt file
    try:
        with open('grades.txt', 'r') as file:
            for line in file:
                # Split the line into components
                student_id, section, grade = line.strip().split('\t')
                section = int(section)  # Convert section to integer
                
                # Convert grade to numeric score
                numeric_grade = grade_to_score.get(grade, None)
                if numeric_grade is None:
                    print(f"Invalid grade '{grade}' found for student {student_id}. Skipping.")
                    continue
                
                # Add the grade to the appropriate section
                if section not in section_grades:
                    section_grades[section] = []
                section_grades[section].append(numeric_grade)
    except FileNotFoundError:
        print("Error: grades.txt file not found.")
        return
    
    # Calculate and print averages
    for section, grades in sorted(section_grades.items()):
        average = sum(grades) / len(grades)
        print(f"Section {section} average: {average:.3f}")

if __name__ == "__main__":
    main()
