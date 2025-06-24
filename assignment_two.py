# Assignment Two: Inventory Management
# Name: ______________________
# Date: ______________________

# Initial stock items (item name and quantity)
stock = [
    {"item": "Pens", "quantity": 20},
    {"item": "Notebooks", "quantity": 15},
    {"item": "Markers", "quantity": 10},
    {"item": "Erasers", "quantity": 25}
]

# Function to display stock items
def display_stock(stock_list):
    print("\nCurrent Stock:")
    for s in stock_list:
        print(f"Item: {s['item']}, Quantity: {s['quantity']}")

display_stock(stock)

# Function to update stock quantity
def update_stock(stock_list, item_name, new_quantity):
    for s in stock_list:
        if s["item"].lower() == item_name.lower():
            s["quantity"] = new_quantity
            print(f"Updated {item_name} to quantity {new_quantity}.")
            return
    print(f"Item '{item_name}' not found in stock.")

# Example update (you can change these values to test)
update_stock(stock, "Pens", 30)

display_stock(stock) 