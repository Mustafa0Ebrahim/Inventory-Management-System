import matplotlib.pyplot as plt

class Product:
    def __init__(self, name, quantity, price, category):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category = category

    def __str__(self):
        return f"Name: {self.name}, Quantity: {self.quantity}, Price: {self.price}, Category: {self.category}"


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, name, quantity, price, category):
        product = Product(name, quantity, price, category)
        self.products.append(product)
        print(f"✅ Product '{name}' added successfully.")

    def edit_product(self, name, quantity, price, category):
        for product in self.products:
            if product.name == name:
                product.quantity = quantity
                product.price = price
                product.category = category
                print(f"✏️ Product '{name}' updated successfully.")
                return
        print(f"❌ Product '{name}' not found.")

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"🗑️ Product '{name}' removed.")
                return
        print(f"❌ Product '{name}' not found.")

    def sell_product(self, name, quantity):
        for product in self.products:
            if product.name == name:
                if product.quantity >= quantity:
                    product.quantity -= quantity
                    print(f"🛒 Sold {quantity} of '{name}'. Remaining: {product.quantity}")
                else:
                    print(f"⚠️ Not enough stock. Available: {product.quantity}")
                return
        print(f"❌ Product '{name}' not found.")

    def view_products(self):
        if not self.products:
            print("ℹ️ No products available.")
            return
        for product in self.products:
            print(product)

    def search_product(self, name):
        for product in self.products:
            if product.name == name:
                print("🔍 Found:", product)
                return
        print(f"❌ Product '{name}' not found.")

    def sort_products(self, by):
        if by == "name":
            self.products.sort(key=lambda x: x.name)
        elif by == "price":
            self.products.sort(key=lambda x: x.price)
        elif by == "quantity":
            self.products.sort(key=lambda x: x.quantity)
        else:
            print("⚠️ Invalid sort criteria.")

    def filter_products(self, category, min_price=None, max_price=None):
        filtered = [p for p in self.products if p.category == category]
        if min_price is not None:
            filtered = [p for p in filtered if p.price >= min_price]
        if max_price is not None:
            filtered = [p for p in filtered if p.price <= max_price]

        if not filtered:
            print("❌ No matching products found.")
            return

        for product in filtered:
            print(product)

    def total_value(self):
        total = sum(p.price * p.quantity for p in self.products)
        print(f"💰 Total Inventory Value: {total:.2f}")

    def load_data(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    name, quantity, price, category = line.strip().split(',')
                    self.add_product(name, int(quantity), float(price), category)
            print("📂 Data loaded successfully.")
        except FileNotFoundError:
            print("❌ File not found.")
        except Exception as e:
            print(f"❌ Error loading data: {e}")

    def save_data(self, filename):
        try:
            with open(filename, 'w') as file:
                for product in self.products:
                    file.write(f"{product.name},{product.quantity},{product.price},{product.category}\n")
            print("💾 Data saved successfully.")
        except Exception as e:
            print(f"❌ Error saving data: {e}")

    def stock_visualization(self):
        if not self.products:
            print("📊 No data to visualize.")
            return

        names = [p.name for p in self.products]
        quantities = [p.quantity for p in self.products]

        plt.figure(figsize=(10, 5))
        plt.bar(names, quantities, color='lightblue')
        plt.xlabel("Product Names")
        plt.ylabel("Quantities")
        plt.title("Stock Visualization")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def get_positive_int(self, prompt):
        while True:
            try:
                val = int(input(prompt))
                if val < 0:
                    raise ValueError("Value cannot be negative.")
                return val
            except ValueError as e:
                print("⚠️ Invalid input:", e)

    def get_positive_float(self, prompt):
        while True:
            try:
                val = float(input(prompt))
                if val < 0:
                    raise ValueError("Value cannot be negative.")
                return val
            except ValueError as e:
                print("⚠️ Invalid input:", e)

    def cli(self):
        while True:
            print("\n📦 Inventory Management System")
            print("1. Add Product")
            print("2. Edit Product")
            print("3. Remove Product")
            print("4. Sell Product")
            print("5. View Products")
            print("6. Search Product")
            print("7. Sort Products")
            print("8. Filter Products")
            print("9. Total Inventory Value")
            print("10. Load Data from File")
            print("11. Save Data to File")
            print("12. Visualize Stock")
            print("13. Exit")

            choice = input("Choose option: ")

            if choice == '1':
                name = input("Product Name: ")
                quantity = self.get_positive_int("Quantity: ")
                price = self.get_positive_float("Price: ")
                category = input("Category: ")
                self.add_product(name, quantity, price, category)
            elif choice == '2':
                name = input("Product Name to Edit: ")
                quantity = self.get_positive_int("New Quantity: ")
                price = self.get_positive_float("New Price: ")
                category = input("New Category: ")
                self.edit_product(name, quantity, price, category)
            elif choice == '3':
                name = input("Product Name to Remove: ")
                self.remove_product(name)
            elif choice == '4':
                name = input("Product Name to Sell: ")
                quantity = self.get_positive_int("Quantity to Sell: ")
                self.sell_product(name, quantity)
            elif choice == '5':
                self.view_products()
            elif choice == '6':
                name = input("Search Product Name: ")
                self.search_product(name)
            elif choice == '7':
                by = input("Sort by (name/price/quantity): ").lower()
                self.sort_products(by)
            elif choice == '8':
                category = input("Category to Filter: ")
                self.filter_products(category)
            elif choice == '9':
                self.total_inventory_value()
            elif choice == '10':
                filename = input("Filename to Load From: ")
                self.load_data(filename)
            elif choice == '11':
                filename = input("Filename to Save To: ")
                self.save_data(filename)
            elif choice == '12':
                self.stock_visualization()
            elif choice == '13':
                print("👋 Exiting. Thank you!")
                break
            else:
                print("⚠️ Invalid option. Try again.")


if __name__ == "__main__":
    Inventory().cli()
# This code implements a simple inventory management system with a command-line interface.
Inventory.cli()