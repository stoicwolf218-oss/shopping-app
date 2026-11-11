"""Checkout module for the online shopping application."""


def calculate_total(items):
    """Calculate the total price of all items in the cart.

    Args:
        items: A list of dictionaries, each with 'price' and 'quantity'.

    Returns:
        The total price as a float.
    """
    total = sum(item["price"] * item["quantity"] for item in items)
    return total


def checkout(cart, customer):
    """Process the checkout for a customer's cart.

    Args:
        cart: A list of items in the shopping cart.
        customer: A dictionary with customer details.

    Returns:
        The final total amount to charge.
    """
    return calculate_total(cart)
