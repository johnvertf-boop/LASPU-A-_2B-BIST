# --------------------------------------------
# MODULE: orders.py
# Gets the customer's orders
# --------------------------------------------

from display import display_menu


def get_orders(menu):
    """
    Get customer orders by letting the customer
    select a menu item and enter the quantity.

    Args:
        menu: Dictionary containing menu items and their prices.

    Returns:
        list: A list containing the customer's orders.
    """
    orders = []

    while True:
        display_menu(menu)

        while True:
            choice = input("Enter menu item number: ")

            try:
                choice = int(choice)

                if 1 <= choice <= len(menu):
                    break
                else:
                    print("Invalid choice. Please choose from the menu.")

            except ValueError:
                print("Please enter a valid number.")

        item_list = list(menu.keys())
        selected_item = item_list[choice - 1]

        while True:
            quantity = input("Enter quantity: ")

            try:
                quantity = int(quantity)

                if quantity > 0:
                    break
                else:
                    print("Quantity must be greater than zero.")

            except ValueError:
                print("Please enter a valid quantity.")

        price = menu[selected_item]
        item_total = price * quantity

        orders.append({
            "item": selected_item,
            "quantity": quantity,
            "price": price,
            "total": item_total
        })

        print(f"\n{selected_item} has been added to your order.")

        while True:
            another = input(
                "Do you want to order another item? (yes/no): "
            ).lower()

            if another == "yes" or another == "y":
                break

            elif another == "no" or another == "n":
                return orders

            else:
                print("Please enter yes or no.")
