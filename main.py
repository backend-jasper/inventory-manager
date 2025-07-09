import json

# ------------------
# Load user accounts
# ------------------
def load_users():
    with open("users.json", "r") as f:
        return json.load(f)

# ------------------
# Login System
# ------------------
def login():
    users = load_users()
    print("🔐 Login to Inventory Manager")
    username = input("Username: ")
    password = input("Password: ")

    for user in users:
        if user["username"] == username and user["password"] == password:
            print(f"\n✅ Welcome, {username}!\n")
            return user
    print("\n❌ Invalid credentials. Try again.\n")
    return None

# ------------------
# Load & Save Inventory
# ------------------
def load_inventory():
    try:
        with open("inventory.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_inventory(products):
    with open("inventory.json", "w") as f:
        json.dump(products, f, indent=2)

# ------------------
# View Inventory
# ------------------
def view_inventory():
    products = load_inventory()

    if not products:
        print("\n📦 Inventory is empty.\n")
        return

    print("\n📋 Current Inventory:\n")
    for idx, item in enumerate(products, start=1):
        print(f"{idx}. Name: {item['name']}")
        print(f"   Quantity: {item['quantity']}")
        print(f"   Category: {item['category']}\n")

# ------------------
# Add Product
# ------------------
def add_product():
    name = input("📌 Product name: ").strip()
    quantity = input("🔢 Quantity: ").strip()
    category = input("📂 Category: ").strip()

    if not name or not quantity.isdigit() or not category:
        print("❌ Invalid input. Product not added.\n")
        return

    products = load_inventory()
    products.append({
        "name": name,
        "quantity": int(quantity),
        "category": category
    })
    save_inventory(products)
    print("✅ Product added successfully!\n")

# ------------------
# Edit Product
# ------------------
def edit_product():
    products = load_inventory()
    if not products:
        print("📦 Inventory is empty. Nothing to edit.\n")
        return

    view_inventory()
    choice = input("🔢 Enter product number to edit: ")

    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(products):
        print("❌ Invalid selection.\n")
        return

    idx = int(choice) - 1
    product = products[idx]

    print(f"\nEditing '{product['name']}'")
    new_name = input(f"📌 New name (leave blank to keep '{product['name']}'): ")
    new_quantity = input(f"🔢 New quantity (leave blank to keep '{product['quantity']}'): ")
    new_category = input(f"📂 New category (leave blank to keep '{product['category']}'): ")

    if new_name.strip():
        product['name'] = new_name.strip()
    if new_quantity.isdigit():
        product['quantity'] = int(new_quantity)
    if new_category.strip():
        product['category'] = new_category.strip()

    save_inventory(products)
    print("✅ Product updated successfully!\n")

# ------------------
# Delete Product
# ------------------
def delete_product():
    products = load_inventory()
    if not products:
        print("📦 Inventory is empty. Nothing to delete.\n")
        return

    view_inventory()
    choice = input("❌ Enter product number to delete: ")

    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(products):
        print("❌ Invalid selection.\n")
        return

    idx = int(choice) - 1
    removed = products.pop(idx)
    save_inventory(products)
    print(f"✅ '{removed['name']}' deleted from inventory.\n")

# ------------------
# Main Menu
# ------------------
def show_menu(user):
    while True:
        print("📦 Inventory Manager Menu")
        print("1. View Inventory")
        print("2. Add Product")
        print("3. Edit Product")
        print("4. Delete Product")
        print("5. Logout")
        choice = input("Enter choice (1-5): ")

        if choice == "1":
            view_inventory()
        elif choice == "2":
            add_product()
        elif choice == "3":
            edit_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            print("🚪 Logged out.\n")
            break
        else:
            print("❌ Invalid option. Try again.\n")

# ------------------
# Launch App
# ------------------
if __name__ == "__main__":
    user = None
    while not user:
        user = login()
    show_menu(user)
