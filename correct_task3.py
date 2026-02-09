def average_valid_measurements(values):
    total = 0
    valid_count = 0

    for v in values:
        if v is not None:
            try:
                val = float(v)
                total += val
                valid_count += 1
            except ValueError:
                continue

    if valid_count == 0:
        return 0.0

    return total / valid_count