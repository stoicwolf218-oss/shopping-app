# Shopping App

An online shopping application for the Collaborative Software Development exercise (Exercise 2).

## Features

- Shopping cart with item prices and quantities.
- Checkout with total calculation.

## Usage

```python
from checkout import checkout

cart = [{"price": 50.0, "quantity": 2}]
customer = {"is_student": False}
print(checkout(cart, customer))  # 100.0
```
