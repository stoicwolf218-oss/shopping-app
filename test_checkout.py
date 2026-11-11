"""Tests for the checkout module."""

from checkout import apply_student_discount, calculate_total, checkout


def test_student_receives_10_percent_discount():
    assert apply_student_discount(100, True) == 90.0


def test_non_student_pays_original_price():
    assert apply_student_discount(100, False) == 100.0


def test_final_amount_is_correct_for_student():
    cart = [{"price": 50.0, "quantity": 2}]
    customer = {"is_student": True}
    assert checkout(cart, customer) == 90.0


def test_final_amount_is_correct_for_non_student():
    cart = [{"price": 50.0, "quantity": 2}]
    customer = {"is_student": False}
    assert checkout(cart, customer) == 100.0
