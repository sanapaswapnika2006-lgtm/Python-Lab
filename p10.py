
def merge_inventory(*stores):
    inventory = {}

    for store in stores:
        for product, quantity in store.items():
            inventory[product] = inventory.get(product, 0) + quantity

    return inventory


def check_product(inventory, product):
    if product in inventory:
        print(product, "is available.")
        print("Quantity:", inventory.get(product, 0))
    else:
        print(product, "is not available.")


def low_stock(inventory, limit=10):
    return {
        product: quantity
        for product, quantity in inventory.items()
        if quantity < limit
    }


# Inventory at different stores
store1 = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 8
}

store2 = {
    "Laptop": 5,
    "Mouse": 15,
    "Monitor": 12
}

store3 = {
    "Keyboard": 7,
    "Monitor": 6
}

# Merge all store inventories
inventory = merge_inventory(store1, store2, store3)

print("Combined Inventory:", inventory)

# Check whether a product exists
check_product(inventory, "Laptop")
check_product(inventory, "Printer")

# Find products with low stock
print("Low Stock Products:", low_stock(inventory))

# Update inventory using the update() method
inventory.update({"Printer": 4, "Mouse": 5})

print("Updated Inventory:", inventory)
