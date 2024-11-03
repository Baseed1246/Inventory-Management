class Item:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"Item: {self.name}, Quantity: {self.quantity}, Price: ${self.price:.2f}"

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity, price):
        if name in self.items:
            self.items[name].quantity += quantity
        else:
            self.items[name] = Item(name, quantity, price)
        print(f"Added {quantity} of {name}.")

    def update_item(self, name, quantity, price):
        if name in self.items:
            self.items[name].quantity = quantity
            self.items[name].price = price
            print(f"Updated {name}. New Quantity: {quantity}, New Price: ${price:.2f}.")
        else:
            print(f"Item {name} does not exist.")

    def delete_item(self, name):
        if name in self.items:
            del self.items[name]
            print(f"Deleted item {name}.")
        else:
            print(f"Item {name} does not exist.")

    def view_inventory(self):
        if not self.items:
            print("Inventory is empty.")
        else:
            for item in self.items.values():
                print(item)

def main():
    inventory = Inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Delete Item")
        print("4. View Inventory")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            price = float(input("Enter item price: "))
            inventory.add_item(name, quantity, price)

        elif choice == '2':
            name = input("Enter item name to update: ")
            quantity = int(input("Enter new item quantity: "))
            price = float(input("Enter new item price: "))
            inventory.update_item(name, quantity, price)

        elif choice == '3':
            name = input("Enter item name to delete: ")
            inventory.delete_item(name)

        elif choice == '4':
            inventory.view_inventory()

        elif choice == '5':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
