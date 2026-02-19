def check_password_strength(password):
    has_digit = False
    has_special = False
    special_chars = "@#$"
    
    # Check minimum length
    if len(password) < 8:
        return "Weak Password ❌ (Minimum length should be 8 characters)"
    
    # Loop through each character
    for char in password:
        if char.isdigit():
            has_digit = True
        if char in special_chars:
            has_special = True
    
    # Validate conditions
    if has_digit and has_special:
        return "Strong Password ✅"
    else:
        return "Weak Password ❌ (Must contain at least one digit and one special character @#$)"


# Example usage
user_password = input("Enter your password: ")
result = check_password_strength(user_password)
print(result)
