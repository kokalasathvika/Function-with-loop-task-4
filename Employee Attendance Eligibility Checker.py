def check_attendance(attendance_list):
    present_count = 0
    
    # Count number of "P" (Present)
    for day in attendance_list:
        if day.upper() == "P":
            present_count += 1
    
    total_days = len(attendance_list)
    
    if total_days == 0:
        return 0, "No Attendance Data"
    
    percentage = (present_count / total_days) * 100
    
    if percentage >= 75:
        return percentage, "Eligible"
    else:
        return percentage, "Not Eligible"


# Sample attendance list
attendance = ["P", "A", "P", "P", "A", "P", "P", "P"]

# Function call
percent, status = check_attendance(attendance)

print(f"Attendance Percentage: {percent:.2f}%")
print("Status:", status)
