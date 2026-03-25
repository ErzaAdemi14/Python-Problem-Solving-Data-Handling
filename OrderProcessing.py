def process_orders(orders):
    valid_orders = []

    for order in orders:
        if order["price"] > 0 and order["quantity"] > 0:
            total_value = order["price"] * order["quantity"]

            valid_order = {
                "order_id": order["order_id"],
                "price": order["price"],
                "quantity": order["quantity"],
                "total_value": total_value
            }

            valid_orders.append(valid_order)

    return valid_orders

orders = [
    {"order_id": 1, "price": 50, "quantity": 2},
    {"order_id": 2, "price": -10, "quantity": 1},
    {"order_id": 3, "price": 30, "quantity": 0},
    {"order_id": 4, "price": 20, "quantity": 3}
]

result = process_orders(orders)
print(result)