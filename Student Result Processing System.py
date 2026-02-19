def process_result(marks):
    total = 0
    
    # Calculate total using loop
    for mark in marks:
        total += mark
    
    average = total / len(marks)
    
    # Determine result
    if average >= 50:
        return average, "Pass"
    else:
        return average, "Fail"


# Sample marks list
student_marks = [60, 45, 70, 55, 40]

# Function call
avg, result = process_result(student_marks)

print("Average Marks:", avg)
print("Result:", result)
