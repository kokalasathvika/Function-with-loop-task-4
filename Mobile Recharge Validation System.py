def validate_recharge(amount):
    valid_plans = [199, 299, 399, 599]
    
    if amount < 50:
        print("❌ Recharge amount must be at least ₹50.")
        return False
    elif amount not in valid_plans:
        print("❌ Invalid plan selected.")
        print("Available plans are:", valid_plans)
        return False
    else:
        print("✅ Recharge successful!")
        return True


# Retry system using while loop
while True:
    try:
        user_amount = int(input("Enter recharge amount: ₹"))
        
        if validate_recharge(user_amount):
            break   # Exit loop if recharge is valid
        else:
            print("Please try again.\n")
            
    except ValueError:
        print("❌ Please enter a valid numeric amount.\n")
