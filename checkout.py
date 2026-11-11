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


def apply_student_discount(total, is_student):
    """Apply a 10% discount for eligible students.

    Args:
        total: The original purchase total.
        is_student: True if the customer is a student.

    Returns:
        The discounted total (10% off) for students, otherwise the original total.
    """
    if is_student:
        return total * 0.90
    return total


def checkout(cart, customer):
    """Process the checkout for a customer's cart.

    Args:
        cart: A list of items in the shopping cart.
        customer: A dictionary with customer details (e.g. is_student).

    Returns:
        The final total amount to charge.
    """
    total = calculate_total(cart)
    is_student = customer.get("is_student", False)
    return apply_student_discount(total, is_student)
