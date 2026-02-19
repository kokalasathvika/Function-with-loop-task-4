def check_inventory(products):
    for product, quantity in products.items():
        if quantity < 15:
            print(f"⚠️ Reorder Alert: {product} (Stock: {quantity})")
        else:
            print(f"✅ Stock OK: {product} (Stock: {quantity})")


# Sample inventory dictionary
inventory = {
    "Rice": 10,
    "Wheat": 25,
    "Sugar": 12,
    "Oil": 30,
    "Salt": 8
}

# Call the function
check_inventory(inventory)
