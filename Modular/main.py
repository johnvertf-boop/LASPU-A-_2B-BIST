# ================================================
# PRELIM PERFORMANCE TASK
# LASPUÑA JVL RESTOVAR RESTAURANT ORDERING SYSTEM
# main.py - runs the program (MODULAR VERSION)
# ================================================

from menu import get_menu
from display import display_welcome, display_menu, display_receipt
from orders import get_orders
from calculation import calculate_total


def main():
    """Run the main ordering process of RESTOVAR."""
    menu = get_menu()

    display_welcome()
    display_menu(menu)

    # Ask the customer if they want to order
    while True:
        answer = input("\nDo you want to order? (yes/no): ").lower()

        if answer == "yes" or answer == "y":
            break

        elif answer == "no" or answer == "n":
            print("\nThank you for visiting RESTOVAR!")
            print("Have a great day!")
            return

        else:
            print("Please enter yes or no.")

    orders = get_orders(menu)
    total = calculate_total(orders)
    display_receipt(orders, total)


if __name__ == "__main__":
    main()
