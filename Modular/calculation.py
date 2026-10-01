# --------------------------------------------
# MODULE: calculation.py
# Computes the total of the order
# --------------------------------------------

def calculate_total(orders):
    """
    Calculate the total amount of all items ordered.

    Args:
        orders: List containing the customer's orders.

    Returns:
        float: The total amount of the orders.
    """
    total = 0

    for order in orders:
        total += order["total"]

    return total
