def calculate_fare(distance, peak_hour):
    base_fare = 50
    per_km_rate = 12
    
    fare = base_fare + (distance * per_km_rate)
    
    if peak_hour:
        fare += fare * 0.25   # 25% extra
    
    return fare


# Retry system using while loop
while True:
    try:
        distance = float(input("Enter distance travelled (in km): "))
        peak_input = input("Is it peak hour? (yes/no): ").lower()
        
        if peak_input == "yes":
            peak = True
        elif peak_input == "no":
            peak = False
        else:
            print("❌ Please enter 'yes' or 'no' for peak hour.\n")
            continue
        
        total_fare = calculate_fare(distance, peak)
        
        print(f"🚖 Total Cab Fare: ₹{total_fare:.2f}")
        break   # Exit loop after successful calculation
    
    except ValueError:
        print("❌ Please enter a valid numeric distance.\n")
