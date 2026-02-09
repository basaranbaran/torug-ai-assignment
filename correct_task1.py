def calculate_average_order_value(orders):
    total = 0
    valid_count = 0

    for order in orders:
        if order["status"] != "cancelled":
            total += order["amount"]
            valid_count += 1

    if valid_count == 0:
        return 0.0

    else:
        return total / valid_count