def normalize_numbers(numbers):
    if not numbers:
        raise ValueError("List is empty")
    min_val, max_val = min(numbers), max(numbers)
    if max_val == min_val:
        return [0.0] * len(numbers)
    return [(x - min_val) / (max_val - min_val) for x in numbers]


def filter_outliers(numbers, min_value, max_value):
    return [x for x in numbers if min_value <= x <= max_value]


def calculate_statistics(numbers):
    if not numbers:
        raise ValueError("List is empty")
    stats = {"min": min(numbers), "max": max(numbers), 
             "average": sum(numbers) / len(numbers)}
    return stats
