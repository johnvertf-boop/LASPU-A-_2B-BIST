# --------------------------------------------
# MODULE: display.py
# Functions that print things on the screen
# --------------------------------------------

def display_welcome():
    """Display the welcome message of RESTOVAR Restaurant and Bar."""
    print("==========================================")
    print("             WELCOME TO")
    print("               RESTOVAR")
    print("          RESTAURANT AND BAR")
    print("==========================================")


def display_menu(menu):
    """
    Display all menu items with their prices.

    Args:
        menu: Dictionary containing menu items and their prices.
    """
    print("\n==========================================")
    print("              RESTOVAR MENU")
    print("==========================================")

    number = 1

    for item, price in menu.items():
        print(f"{number}. {item:<25} ₱{price:.2f}")
        number += 1

    print("==========================================")


def display_receipt(orders, total):
    """
    Display the official receipt.

    Args:
        orders: List containing the customer's orders.
        total: The total amount of the order.
    """
    print("\n\n")
    print("==========================================")
    print("                 RESTOVAR")
    print("             RESTAURANT AND BAR")
    print("              OFFICIAL RECEIPT")
    print("==========================================")

    print(f"{'ITEM':<20} {'QTY':>4} {'PRICE':>10} {'TOTAL':>10}")
    print("------------------------------------------")

    for order in orders:
        print(
            f"{order['item']:<20}"
            f"{order['quantity']:>4}"
            f"₱{order['price']:>9.2f}"
            f"₱{order['total']:>9.2f}"
        )

    print("------------------------------------------")
    print(f"{'TOTAL AMOUNT':<30} ₱{total:>9.2f}")
    print("==========================================")
    print("          Thank you for dining")
    print("                at RESTOVAR!")
    print("==========================================")
