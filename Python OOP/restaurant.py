# ================================================
# RESTOVAR CLASSES (restaurant.py)
# LASPUÑA JVL RESTOVAR RESTAURANT ORDERING SYSTEM
# ================================================
#
# OOP concepts used:
#   - Classes and Objects
#   - Encapsulation (private attributes + properties)
#   - Abstraction (each class hides its own details)
#   - Composition (Menu has MenuItems, Order has OrderItems)
#   - Inheritance (Drink and Food extend MenuItem)
#   - Polymorphism (each category overrides describe())
# ================================================


# --------------------------------------------
# CLASS: MenuItem (Parent / Base Class)
# --------------------------------------------
class MenuItem:
    """Represents a single item on the restaurant menu."""

    def __init__(self, name, price):
        self._name = name  # protected attribute
        self._price = price  # protected attribute

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    def describe(self):
        """Return a short description of the item (overridden by children)."""
        return f"{self._name:<25} ₱{self._price:.2f}"


# --------------------------------------------
# CLASS: Food (Child of MenuItem) - Inheritance
# --------------------------------------------
class Food(MenuItem):
    """A food item on the menu."""

    def describe(self):
        return f"{self._name:<25} ₱{self._price:.2f}"


# --------------------------------------------
# CLASS: Drink (Child of MenuItem) - Inheritance
# --------------------------------------------
class Drink(MenuItem):
    """A drink item on the menu."""

    def describe(self):
        return f"{self._name:<25} ₱{self._price:.2f}"


# --------------------------------------------
# CLASS: Menu
# --------------------------------------------
class Menu:
    """Holds and displays all MenuItem objects."""

    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def get_item(self, number):
        """Return the MenuItem at the given menu number (1-based)."""
        return self._items[number - 1]

    def size(self):
        return len(self._items)

    def display(self):
        print("\n==========================================")
        print("              RESTOVAR MENU")
        print("==========================================")

        for number, item in enumerate(self._items, start=1):
            print(f"{number}. {item.describe()}")

        print("==========================================")


# --------------------------------------------
# CLASS: OrderItem
# --------------------------------------------
class OrderItem:
    """Represents one line in an order (an item and its quantity)."""

    def __init__(self, menu_item, quantity):
        self._menu_item = menu_item
        self._quantity = quantity

    @property
    def name(self):
        return self._menu_item.name

    @property
    def price(self):
        return self._menu_item.price

    @property
    def quantity(self):
        return self._quantity

    @property
    def total(self):
        return self._menu_item.price * self._quantity


# --------------------------------------------
# CLASS: Order
# --------------------------------------------
class Order:
    """Represents a customer's entire order."""

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    def add_item(self, menu_item, quantity):
        self._items.append(OrderItem(menu_item, quantity))

    def calculate_total(self):
        return sum(item.total for item in self._items)


# --------------------------------------------
# CLASS: Receipt
# --------------------------------------------
class Receipt:
    """Prints the official receipt for an Order."""

    def __init__(self, order):
        self._order = order

    def display(self):
        print("\n\n")
        print("==========================================")
        print("                 RESTOVAR")
        print("             RESTAURANT AND BAR")
        print("              OFFICIAL RECEIPT")
        print("==========================================")

        print(f"{'ITEM':<20} {'QTY':>4} {'PRICE':>10} {'TOTAL':>10}")
        print("------------------------------------------")

        for item in self._order.items:
            print(
                f"{item.name:<20}"
                f"{item.quantity:>4}"
                f"₱{item.price:>9.2f}"
                f"₱{item.total:>9.2f}"
            )

        print("------------------------------------------")
        print(f"{'TOTAL AMOUNT':<30} ₱{self._order.calculate_total():>9.2f}")
        print("==========================================")
        print("          Thank you for dining")
        print("                at RESTOVAR!")
        print("==========================================")


# --------------------------------------------
# CLASS: Restaurant (Main System)
# --------------------------------------------
class Restaurant:
    """Controls the whole RESTOVAR ordering process."""

    def __init__(self):
        self._menu = Menu()
        self._load_menu()

    # ---------- Setup ----------
    def _load_menu(self):
        """Fill the menu with Food and Drink objects."""
        self._menu.add_item(Food("Chicken Meal", 120.00))
        self._menu.add_item(Food("Burger", 85.00))
        self._menu.add_item(Food("Pasta", 110.00))
        self._menu.add_item(Food("French Fries", 60.00))
        self._menu.add_item(Food("Pizza", 180.00))
        self._menu.add_item(Drink("Iced Tea", 45.00))
        self._menu.add_item(Drink("Soft Drink", 40.00))
        self._menu.add_item(Drink("Coffee", 55.00))

    # ---------- Display ----------
    def display_welcome(self):
        print("==========================================")
        print("             WELCOME TO")
        print("               RESTOVAR")
        print("          RESTAURANT AND BAR")
        print("==========================================")

    # ---------- Input helpers ----------
    def _ask_yes_no(self, message):
        """Keep asking until the user answers yes or no. Returns True/False."""
        while True:
            answer = input(message).lower()

            if answer in ("yes", "y"):
                return True
            elif answer in ("no", "n"):
                return False
            else:
                print("Please enter yes or no.")

    def _ask_menu_choice(self):
        """Ask for a valid menu number and return the chosen MenuItem."""
        while True:
            choice = input("Enter menu item number: ")

            try:
                choice = int(choice)

                if 1 <= choice <= self._menu.size():
                    return self._menu.get_item(choice)
                else:
                    print("Invalid choice. Please choose from the menu.")

            except ValueError:
                print("Please enter a valid number.")

    def _ask_quantity(self):
        """Ask for a valid quantity greater than zero."""
        while True:
            quantity = input("Enter quantity: ")

            try:
                quantity = int(quantity)

                if quantity > 0:
                    return quantity
                else:
                    print("Quantity must be greater than zero.")

            except ValueError:
                print("Please enter a valid quantity.")

    # ---------- Ordering ----------
    def take_order(self):
        """Take the customer's order and return an Order object."""
        order = Order()

        while True:
            self._menu.display()

            selected_item = self._ask_menu_choice()
            quantity = self._ask_quantity()

            order.add_item(selected_item, quantity)
            print(f"\n{selected_item.name} has been added to your order.")

            if not self._ask_yes_no("Do you want to order another item? (yes/no): "):
                return order

    # ---------- Run ----------
    def run(self):
        """Run the full ordering process."""
        self.display_welcome()
        self._menu.display()

        if not self._ask_yes_no("\nDo you want to order? (yes/no): "):
            print("\nThank you for visiting RESTOVAR!")
            print("Have a great day!")
            return

        order = self.take_order()

        receipt = Receipt(order)
        receipt.display()
